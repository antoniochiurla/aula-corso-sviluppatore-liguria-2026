from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout

from .models import Task, BugTask, FeatureTask
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Recuperiamo tutti i task dal database
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})

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


def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'CL' if task.status == 'AP' else 'AP'
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def logout_view(request):
    logout(request)