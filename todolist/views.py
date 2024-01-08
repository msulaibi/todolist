from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user #commit=False to delay save to get user request first
            form.save()
            messages.success(request, "New Task Add")
            return redirect('todolist')
    else:
        #all_tasks = TaskList.objects.all
        all_tasks = TaskList.objects.filter(manage = request.user)
        context= {
            'all_tasks': all_tasks
        }
        return render(request, 'todolist.html', context)

@login_required
def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        task.save()
        messages.success(request, "Task Deleted")
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed!")
    return redirect('todolist') 

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task':task})

@login_required    
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed!")
    return redirect('todolist')
    
@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed!")    
    return redirect('todolist')