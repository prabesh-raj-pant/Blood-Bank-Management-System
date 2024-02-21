
from django.shortcuts import render,redirect
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import *
from .serializer import *
from django.views import *
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import ProfileForm
from django.shortcuts import render
from .models import Donor


def index(request):
    return render(request,'index.html')

@login_required
def about(request):
    return render(request,'about.html')

def index_about(request):
    return render(request,'index_about.html')

@login_required
def donor(request):
    user=request.user
    if request.method == 'POST':
        Donor_Name = request.POST.get('name')
        Donor_Age = request.POST.get('Age') 
        Donor_Address = request.POST.get('Address')
        Donor_BloodType = request.POST.get('bloodType')
        Donor_Phone=request.POST.get('phone')

        # Get the current date and time
        timezone.activate('Asia/Kolkata')
        current_datetime = timezone.now()

        # Check if the email is allowed to submit before 3 months
        allowed_submission_date = current_datetime - timedelta(days=90)

        # Check if there is a previous submission within the last 3 months
        if Donor.objects.filter(Donor_Email=user.email, Donor_DateTime__gte=allowed_submission_date).exists():
            messages.error(request, 'You are not allowed to submit before 3 months.')
            return render(request, 'donor.html')

        donor = Donor()
        donor.Donor_Name = Donor_Name
        donor.Donor_Age = Donor_Age  
        donor.Donor_Address = Donor_Address
        donor.Donor_BloodType = Donor_BloodType
        donor.Donor_Email = user.email
        donor.Donor_Phone=Donor_Phone
        donor.Donor_DateTime = current_datetime
        donor.save()
        messages.success(request, 'Form submitted successfully!')

        return render(request, 'donor.html')

    return render(request, 'donor.html')

def get_object(self, pk):
    try:
        return Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        return HttpResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

@login_required
def bloodrequest(request):
    context={}
    if request.method=='POST':
        Receipent_Name=request.POST.get('name')
        Receipent_Age=request.POST.get('Age')
        Receipent_BloodType=request.POST.get('bloodType')
        Receipent_Address=request.POST.get('address')
        Receipent_Email=request.POST.get('email')
        Receipent_Phone=request.POST.get('phone')
        Receipent_Hospital=request.POST.get('hospital')
        timezone.activate('Asia/Kolkata')
        current_datetime = timezone.now()
        
        receipent=Receipent()
        receipent.Receipent_Name=Receipent_Name
        receipent.Receipent_Age=Receipent_Age
        receipent.Receipent_BloodType=Receipent_BloodType
        receipent.Receipent_Address=Receipent_Address
        receipent.Receipent_Email=Receipent_Email
        receipent.Receipent_Phone=Receipent_Phone
        receipent.Receipent_Hospital=Receipent_Hospital
        
        receipent.Receipent_DateTime = current_datetime
        receipent.save()
        messages.success(request, 'Form submitted successfully!')
        donors = Donor.objects.filter(Donor_BloodType=Receipent_BloodType)
        
        context = {
            'donors': donors,
        }
    
    return render(request, 'bloodrequest.html', context)



def custom_logout(request):
    # logout(request)
    return render(request, 'register/auth.html')






def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        # Split the email to set the username
        username = email.split('@')[0]
        
        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        messages.success(request, 'Form submitted successfully!')
        return redirect('register')

    return render(request, 'register/auth.html')

class AuthView(View):
    def get(self, request):
        return render(request, 'register/auth.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('admin:index')  
            else:
                return redirect('landing_page')  
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'register/auth.html')

def logout(request):
    django_logout(request)
    return redirect('index')


@login_required
def dashboard(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('dashboard')
        
    donors = Donor.objects.filter(Donor_Email=user.email)
    receipents = Receipent.objects.filter(Receipent_Email=user.email)
    
    context = {
        'user': user,
        'form': form,
        'donors': donors,
        'receipents': receipents,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def edit_donor(request, pk):
        donor = Donor.objects.get(pk=pk)
        if request.method == "POST":
            donor.Donor_Name = request.POST.get('name')
            donor.Donor_Age = request.POST.get('Age')
            donor.Donor_Address = request.POST.get('Address')
            donor.Donor_BloodType = request.POST.get('bloodType')
            donor.Donor_Phone = request.POST.get('phone')
            timezone.activate('Asia/Kolkata')
            donor.Donor_DateTime = timezone.now()
            donor.save()
            return redirect('dashboard')  
        context = {
            'donor': donor
        }
        return render(request, 'edit_donor.html', context)
     
     
@login_required   
def edit_receipent(request, pk):
    try:
        receipent = Receipent.objects.get(pk=pk)
        if request.method == "POST":
            receipent.Receipent_Name = request.POST.get('name')
            receipent.Receipent_Age = request.POST.get('Age')
            receipent.Receipent_Address = request.POST.get('Address')
            receipent.Receipent_BloodType = request.POST.get('bloodType')
            receipent.Receipent_Phone = request.POST.get('phone')
            receipent.Receipent_Hospital = request.POST.get('hospital')
            timezone.activate('Asia/Kolkata')
            receipent.Receipent_DateTime = timezone.now()
            receipent.save()
            return redirect('dashboard')  
        context = {
            'receipent': receipent
        }
        return render(request, 'edit_receipent.html', context)
    except Receipent.DoesNotExist:
        return HttpResponse("no data exist")



def delete_donor(request,pk):
    try:
        donor=Donor.objects.get(pk=pk)
        donor.delete()
        return redirect('dashboard')
    except Donor.DoesNotExist:
        return HttpResponse("no such task exists")


def delete_receipent(request,pk):
    try:
        receipent=Receipent.objects.get(pk=pk)
        receipent.delete()
        return redirect('dashboard')
    except Donor.DoesNotExist:
        return HttpResponse("no such task exists")

@login_required
def landing_page(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None
    return render(request,'landing_page.html')

