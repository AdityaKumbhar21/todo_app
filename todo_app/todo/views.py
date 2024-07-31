from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    todos = Todo.objects.all()
    return render(request, 'todo/home.html',{'todos':todos})


@login_required(login_url='register/')
def add_todo(request):
    if request.method == "POST":
        data = request.POST
        task = data.get('task')
        task_description = data.get('task_description')

        Todo.objects.create(
           user = request.user,
            task = task,
            task_description =  task_description 
        )
        return redirect('home') 

    return render(request,'todo/add_todo.html')



@login_required(login_url='register/')
def edit_todo(request,todo_id):
    todo = Todo.objects.get(pk = todo_id)

    if request.method == 'POST':
        data = request.POST
        task = data.get('task')
        task_description = data.get('task_description')

        todo.task = task
        todo.task_description = task_description

        todo.save()
        return redirect('home')
    
    return render(request,'todo/edit_todo.html',{'todo':todo})


@login_required(login_url='register/')
def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return redirect('home')

@login_required(login_url='register/')
def search_results(request):
    search_query = request.GET.get('search')

    if Todo.objects.filter(task__icontains = search_query):
        todos = Todo.objects.filter(task__icontains = search_query)
    else:
        return render(request,'todo/no_results.html',{'search_query':search_query})
    return render(request,'todo/search_results.html',{'todos':todos,'search_query':search_query})

@login_required(login_url='register/')
def account(request):
    user = request.user
    return render(request,'todo/account.html',{'user':user})


def register_page(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create(
            email = email,
            username = username    
        )

        user.set_password(password)
        user.save()
        messages.success(request, "User registered successfully.")
        return redirect('home')


    return render(request, 'registeration/register.html')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login_page/')

    
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login_page/')  

        else:
            login(request,user) 
            return redirect('home') 
    

    return render(request,'registeration/login.html')


def logout_page(request):
    logout(request)
    return render(request,'todo/logout.html')

