from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    todos = Todo.objects.all()
    return render(request, 'todo/home.html',{'todos':todos})

@login_required
def add_todo(request):
    if request.method == "POST":
        data = request.POST
        task = data.get('task')
        task_description = data.get('task_description')

        Todo.objects.create(
            task = task,
            task_description =  task_description 
        )
        return redirect('home') 

    return render(request,'todo/add_todo.html')

