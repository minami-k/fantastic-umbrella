from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo

def home(request):
    return render(request, 'todo/home.html')

# AUTHENTICATION
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html', { 'form' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                #create_user(username, email=None, password=None, **extra_fields)
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(
                    request, 
                    'todo/signup.html', 
                    {
                        'form': UserCreationForm(),
                        'error':'That username has already been taken.'
                    }
                )
        else:
            #Tell the user that passwords do not match
            return render(
                request, 
                'todo/signup.html', 
                {
                    'form': UserCreationForm(),
                    'error':'Passwords did not match'
                }
            )

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', { 'form' : AuthenticationForm()})
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )

        if user is None:
            return render(
                request, 
                'todo/login.html', 
                { 
                    'form' : AuthenticationForm(),
                    'error':'Username and password are incorrect'
                }
            )
        else:
            login(request, user)
            return redirect('currenttodos')


#TODOS
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/currenttodos.html', { 'todos': todos })

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', { 'form' : TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(
                request, 
                'todo/createtodo.html', 
                {
                    'form': TodoForm(),
                    'error': 'Bad data passed in. Try again'
                }
            )