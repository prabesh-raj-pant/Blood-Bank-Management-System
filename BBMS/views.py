# views.py
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views import *
from django.contrib.auth.models import User, auth

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def donor(request):
    return render(request,'donor.html')

def bloodrequest(request):
    return render(request,'bloodrequest.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()

        return redirect('register')

    return render(request, 'register/auth.html')

class AuthView(View):
    def get(self, request):
        return render(request, 'register/auth.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'register/auth.html', {'error_message': 'Invalid login credentials'})