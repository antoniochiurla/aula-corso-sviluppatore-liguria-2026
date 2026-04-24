from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout

from .models import Task, BugTask, FeatureTask
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Recuperiamo tutti i task dal database
    tasks = Task.objects.all().order_by('-created_at')
    colors = {
        'T': 'primary',
        'B': 'danger',
        'F': 'warning'}
    icons = {
        'T': '...',
        'B': '🐞',
        'F': '⭐'
    }
    context = {
        'tasks': tasks,
        'colors': colors,
        'icons': icons}
    return render(request, 'tasks/index.html', context)

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    bug_task = None
    feature_task = None
    if task.type == 'B':
        bug_task = BugTask.objects.get(pk=task_id)
    if task.type == 'F':
        feature_task = FeatureTask.objects.get(pk=task_id)
    if request.method == "POST":
        bug_task.title = request.POST.get('titolo')
        bug_task.description = request.POST.get('descrizione')
        if task.type == 'B':
            bug_task.severity = request.POST.get('severity')
            bug_task.save()
        elif task.type == 'F':
            feature_task.priority = request.POST.get('priority')
            feature_task.save()
        else:
            task.save()

        return redirect('index')
    context = {
        'tipo': task.type,
        'task': task,
        'bug': bug_task,
        'feature': feature_task,
        'types': {'T': 'Task', 'B': "Bug", 'F': 'Feature'}
        }
    return render(request, 'tasks/add_form.html', context)

@login_required
def add_task(request, tipo):
    if request.method == "POST":
        titolo = request.POST.get('titolo')
        desc = request.POST.get('descrizione')

        if tipo == 'bug':
            BugTask.objects.create(created_by=request.user,title=titolo, description=desc, severity='ME')
        elif tipo == 'feature':
            FeatureTask.objects.create(created_by=request.user,title=titolo, description=desc, priority='2')
        else:
            Task.objects.create(created_by=request.user,title=titolo, description=desc)

        return redirect('index')
    return render(request, 'tasks/add_form.html', {'tipo': tipo})


@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'CL' if task.status == 'AP' else 'AP'
    task.save()
    return redirect('index')


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

@login_required
def logout_view(request):
    logout(request)
