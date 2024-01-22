# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'index' with the name of your index page
    else:
        form = SignupForm()

    return render(request, 'login.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Replace 'index' with the name of your index page
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request,'index.html')
