import random

from django.db.models import Count, Q, OuterRef, Subquery
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.generic import ListView

from .models import Task, BugTask, FeatureTask
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, BugTaskSerializer, FeatureTaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from logging import getLogger

log = getLogger(__name__)

types = {'T': 'Task', 'B': "Bug", 'F': 'Feature'}

colors = {
    'T': 'primary',
    'B': 'danger',
    'F': 'warning'}
icons = {
    'T': '...',
    'B': '🐞',
    'F': '⭐'
}

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny] # Simplified for now

    def perform_create(self, serializer):
        # Default to first user if not authenticated for simplicity in this exercise
        from django.contrib.auth.models import User
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        serializer.save(created_by=user)

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        task = self.get_object()
        task.status = 'CL' if task.status == 'AP' else 'AP'
        task.save()
        return Response({'status': 'task status toggled', 'new_status': task.status})

class BugTaskViewSet(viewsets.ModelViewSet):
    queryset = BugTask.objects.all()
    serializer_class = BugTaskSerializer
    def perform_create(self, serializer):
        from django.contrib.auth.models import User
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        serializer.save(created_by=user)

class FeatureTaskViewSet(viewsets.ModelViewSet):
    queryset = FeatureTask.objects.all()
    serializer_class = FeatureTaskSerializer
    def perform_create(self, serializer):
        from django.contrib.auth.models import User
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        serializer.save(created_by=user)

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    extra_context = {
        'colors': colors,
        'icons': icons}


@login_required
def index(request):
    log.debug(f"Begin of index")
    # select_related carica created_by e assigned_to (FK) con un unico JOIN.
    # prefetch_related carica bugtask e featuretask (reverse OneToOne)
    # con 2 query aggiuntive per tutta la pagina, invece di 2 per ogni task.
    # Con 12 task per pagina: da ~49 query a 5 (1 tasks + 2 prefetch + 1 count + 1 page).
    all_tasks = Task.objects.select_related(
        'created_by', 'assigned_to'
    ).prefetch_related(
        'bugtask', 'featuretask'
    ).order_by('-created_at')
    paginator = Paginator(all_tasks, 12)
    page_obj = paginator.get_page(request.GET.get('page', 1))
    context = {
        'tasks': page_obj,
        'page_obj': page_obj,
        'colors': colors,
        'icons': icons}
    return render(request, 'tasks/index.html', context)

def get_list_of_users():
    return User.objects.all().order_by('username')

@login_required
@permission_required("tasks.change_task", raise_exception=True)
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    bug_task = None
    feature_task = None
    if task.type == 'B':
        bug_task = task.bugtask
    if task.type == 'F':
        feature_task = task.featuretask
    if request.method == "POST":
        title = request.POST.get('titolo')
        description = request.POST.get('descrizione')
        assigned_to_id = request.POST.get('assigned_to')
        if task.type == 'B':
            bug_task.title = title
            bug_task.description = description
            bug_task.assigned_to_id = assigned_to_id
            bug_task.severity = request.POST.get('severity')
            bug_task.save()
        elif task.type == 'F':
            feature_task.title = title
            feature_task.description = description
            feature_task.assigned_to_id = assigned_to_id
            feature_task.priority = request.POST.get('priority')
            feature_task.save()
        else:
            task.title = title
            task.description = description
            task.assigned_to_id = assigned_to_id
            task.save()

        return redirect('index')
    context = {
        'tipo': task.type,
        'task': task,
        'bug': bug_task,
        'feature': feature_task,
        'types': types,
        'users': get_list_of_users()
        }
    return render(request, 'tasks/add_form.html', context)

@login_required
def add_task(request, tipo):
    log.debug("Begin of add_task")
    if request.method == "POST":
        log.debug("POST in add_task")
        titolo = request.POST.get('titolo')
        desc = request.POST.get('descrizione')
        assigned_to_id = request.POST.get('assigned_to')

        log.debug(f"Type of task received: '{tipo}'")
        if tipo == 'B':
            log.debug("Creating a bug task")
            BugTask.objects.create(created_by=request.user,title=titolo, description=desc, severity='ME', assigned_to_id=assigned_to_id)
        elif tipo == 'F':
            log.debug("Creating a feature task")
            FeatureTask.objects.create(created_by=request.user,title=titolo, description=desc, priority='2', assigned_to_id=assigned_to_id)
        else:
            log.debug("Creating a generic task")
            Task.objects.create(created_by=request.user,title=titolo, description=desc, assigned_to_id=assigned_to_id)

        return redirect('index')
    log.debug('GET in add_task')
    context = {
        'tipo': tipo,
        'types': types,
        'users': get_list_of_users()
    }
    return render(request, 'tasks/add_form.html', context)


@login_required
def toggle_task(request, task_id):
    'Cambia lo stato del task'
    task = Task.objects.get(id=task_id)
    if task.status == 'CL':
        if request.user.has_perm('tasks.can_reopen_task'):
            task.status = 'AP'
        else:
            return HttpResponseForbidden("Non puoi riaprire un task, chiedi all'amministratore.")
    else:
        task.status = 'CL'
    task.save()
    return redirect('index')


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

@login_required
def create_sample_tasks(request):
    first_words = ['Primo', 'Secondo', 'Terzo', 'Quarto']
    task_types = ['Task', 'Bug', 'Feature']
    third_words = ['UI', 'DB', 'Template', 'urls']
    word_count = 3
    vocabulary = [
        "hello", "world", "python", "coffee", "sunshine",
        "coding", "random", "simple", "fun", "today",
        "chat", "music", "easy", "bright", "smile",
        "story", "dream", "coffee", "travel", "good"
    ]
    other_words = " ".join(random.choice(vocabulary) for _ in range(word_count))
    for first_word in first_words:
        for task_type in task_types:
            for third_word in third_words:
                title = f"{first_word} {task_type} {other_words} {third_word}"
                description = f"Descrizione per {title}. Altre parole: {other_words}"
                if task_type == 'Task':
                    Task.objects.create(created_by=request.user, title=title, description=description)
                elif task_type == 'Bug':
                    BugTask.objects.create(created_by=request.user, title=title, description=description, severity='ME')
                elif task_type == 'Feature':
                    FeatureTask.objects.create(created_by=request.user, title=title, description=description, priority='2')
    return redirect('index')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def angular_index(request):
    return render(request, 'index.html')


# -----------------------------------------------------------------------
# FEATURE NON OTTIMIZZATE  (da analizzare con la Django Debug Toolbar)
# -----------------------------------------------------------------------

@login_required
def stats(request):
    """
    Dashboard con statistiche sui task.
    Ottimizzato: annotate() calcola i contatori per utente in 1 query,
    Subquery recupera l'id dell'ultimo task senza loop,
    aggregate() produce tutti i totali globali in 1 query.
    Totale: 3 query invece di (4 × N_utenti + 6).
    """
    last_task_subquery = Task.objects.filter(
        created_by=OuterRef('pk')
    ).order_by('-created_at').values('id')[:1]

    users = User.objects.annotate(
        total=Count('tasks'),
        open_count=Count('tasks', filter=Q(tasks__status='AP')),
        closed_count=Count('tasks', filter=Q(tasks__status='CL')),
        last_task_id=Subquery(last_task_subquery),
    ).order_by('username')

    last_task_ids = [u.last_task_id for u in users if u.last_task_id]
    last_tasks_map = {t.id: t for t in Task.objects.filter(id__in=last_task_ids)}

    user_stats = [
        {
            'user': u,
            'total': u.total,
            'open': u.open_count,
            'closed': u.closed_count,
            'last_task': last_tasks_map.get(u.last_task_id),
        }
        for u in users
    ]

    totals = Task.objects.aggregate(
        total_tasks=Count('id'),
        total_open=Count('id', filter=Q(status='AP')),
        total_closed=Count('id', filter=Q(status='CL')),
        total_bugs=Count('id', filter=Q(type='B')),
        total_features=Count('id', filter=Q(type='F')),
        total_generic=Count('id', filter=Q(type='T')),
    )

    context = {'user_stats': user_stats, **totals}
    return render(request, 'tasks/stats.html', context)


@login_required
def task_detail(request, task_id):
    """
    Pagina di dettaglio di un singolo task.
    Ottimizzato: select_related() carica created_by e assigned_to
    in un solo JOIN, eliminando le query aggiuntive per i FK.
    Il creator viene letto direttamente dall'oggetto già caricato
    senza una query separata.
    """
    task = Task.objects.select_related('created_by', 'assigned_to').get(pk=task_id)

    # Non serve più User.objects.get(): task.created_by è già in memoria
    creator = task.created_by

    creator_tasks = Task.objects.filter(created_by=creator).order_by('-created_at')[:5]
    same_type_tasks = Task.objects.filter(type=task.type).exclude(pk=task.pk).order_by('-created_at')[:5]

    bug_task = None
    feature_task = None
    if task.type == 'B':
        bug_task = task.bugtask
    if task.type == 'F':
        feature_task = task.featuretask

    context = {
        'task': task,
        'creator': creator,
        'creator_tasks': creator_tasks,
        'same_type_tasks': same_type_tasks,
        'bug_task': bug_task,
        'feature_task': feature_task,
        'colors': colors,
        'icons': icons,
        'types': types,
    }
    return render(request, 'tasks/task_detail.html', context)


@login_required
def bulk_assign(request):
    """
    Assegna tutti i task aperti a un utente scelto.
    Ottimizzato: QuerySet.update() produce un unico UPDATE SQL
    indipendentemente dal numero di task aperti.
    """
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)

        # Una sola query UPDATE invece di N
        Task.objects.filter(status='AP').update(assigned_to=user)

        return redirect('index')

    users = User.objects.all().order_by('username')
    open_count = Task.objects.filter(status='AP').count()
    context = {
        'users': users,
        'open_count': open_count,
    }
    return render(request, 'tasks/bulk_assign.html', context)