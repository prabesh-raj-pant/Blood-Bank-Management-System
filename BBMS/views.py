from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import SignupForm, LoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['user-email']  # Use the correct form field name
            password = form.cleaned_data['pass1']  # Use the correct form field name
            print("Email:", email)
            print("Password:", password)

            user = authenticate(request, email=email, password=password)
            print("User:", user)

            if user is not None:
                return render(request, 'index.html')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            print("Form errors:", form.errors)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'forms': form})

def signup(request):
    if (request.method) == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            print(user_data)
            register_user = User.objects.create_user(
                first_name=user_data["first_name"], last_name=user_data["last_name"], username=user_data["username"], email=user_data["email"], password=user_data["password"])
            print("test")
            register_user.save()
            return HttpResponseRedirect("/")
    else:
        form = SignupForm()
    return render(request, "register.html", {
        "forms": form
    })


