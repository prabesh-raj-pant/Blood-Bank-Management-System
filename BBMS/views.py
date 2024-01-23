# views.py
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
def signUp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        data=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=pass1)
        data.save()
        return redirect('login')
    return render(request,'login.html')

def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
