from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .models import Task, BugTask, FeatureTask
from django.contrib.auth.decorators import login_required

types = {'T': 'Task', 'B': "Bug", 'F': 'Feature'}

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

def get_list_of_users():
    return User.objects.all().order_by('username')

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
    if request.method == "POST":
        titolo = request.POST.get('titolo')
        desc = request.POST.get('descrizione')
        assigned_to_id = request.POST.get('assigned_to')

        if tipo == 'B':
            BugTask.objects.create(created_by=request.user,title=titolo, description=desc, severity='ME', assigned_to_id=assigned_to_id)
        elif tipo == 'F':
            FeatureTask.objects.create(created_by=request.user,title=titolo, description=desc, priority='2', assigned_to_id=assigned_to_id)
        else:
            Task.objects.create(created_by=request.user,title=titolo, description=desc, assigned_to_id=assigned_to_id)

        return redirect('index')
    context = {
        'tipo': tipo,
        'types': types,
        'users': get_list_of_users()
    }
    return render(request, 'tasks/add_form.html', context)


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
