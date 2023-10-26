from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskEditForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
    })

def completed(request):
    completed_tasks = Task.objects.filter(completado=True)

    return render(request, 'completed.html', {
        'tasks': completed_tasks,
    })

def remaining(request):
    remaining_tasks = Task.objects.filter(completado=False)
    return render(request, 'remaining.html', {
        'tasks': remaining_tasks,
    })

def add_task(request):
    if request.method == "POST":
        nombre = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False

        if nombre != "" and due_date != "" and due_time !="":
            task = Task(
                nombre=nombre,
                description=description,
                due_date=due_date,
                due_time=due_time,
                completado=completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html') 
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {
        "task": task,
    })

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {
        "task": task,
    })


def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completado = not task.completado
        task.save()
        return redirect('home')


def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')
    
def edit_task(request, task_id):
        task = Task.objects.get(pk=task_id)
        if request.method == 'POST':
            form = TaskEditForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TaskEditForm(instance=task)
            
        return render(request, 'edit_task.html', {'form': form, 'task': task})
