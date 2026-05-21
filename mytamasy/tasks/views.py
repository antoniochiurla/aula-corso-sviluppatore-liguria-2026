from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.contrib.auth import logout
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
    # Recuperiamo tutti i task dal database
    tasks = Task.objects.all().order_by('-created_at')
    context = {
        'tasks': tasks,
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
def logout_view(request):
    return logout(request)

def angular_index(request):
    return render(request, 'index.html')