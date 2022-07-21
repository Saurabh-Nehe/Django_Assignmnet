from pydoc import describe
from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Task


# Create your views here.
def show_list(request):
    tasks = Task.objects.order_by('-modified_date')
    return render(request, 'todo_app/show_list.html', {'tasks':tasks})

def delete_task(requst,id):
    print("Here")
    task_to_be_deleted = Task.objects.get(id=id)
    task_to_be_deleted.delete()
    return redirect('todo_list')
    
def update_task(request,id):
    task_to_be_deleted = Task.objects.get(id=id)
    if request.method == "POST":
        obj=task_to_be_deleted
        obj.task_name = request.POST['taskname']
        obj.description=request.POST['description']
        obj.deadline = request.POST['deadline']
        obj.modified_date = timezone.now()
        obj.status = request.POST['status']
        obj.save()
    
    return render(request,'todo_app/update.html', {'task_to_be_deleted':task_to_be_deleted})
    

def add_task(request):
    if request.method == "POST":
        obj = Task()
        obj.task_name = request.POST['taskname']
        obj.description=request.POST['description']
        obj.deadline = request.POST['deadline']
        obj.modified_date = timezone.now()
        obj.status = request.POST['status']
        obj.save()
    
    return render(request, 'todo_app/input.html', {})


