# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import *
from .serializer import *
from django.views import *
from django.contrib.auth.models import User, auth
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import ProfileForm

def index(request):
    return render(request,'index.html')
@login_required
def about(request):
    return render(request,'about.html')

def donor(request):
    user=request.user
    if request.method == 'POST':
        Donor_Name = request.POST.get('name')
        Donor_Age = request.POST.get('Age') 
        Donor_Address = request.POST.get('Address')
        Donor_BloodType = request.POST.get('bloodType')
        Donor_Phone=request.POST.get('phone')

        # Get the current date and time
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
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

 
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
    return redirect('register')


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



class DonorList(APIView):
    def get(self, request):
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DonorDetail(APIView):
    def get_object(self, pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Response()

    def get(self, request, pk):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor)
        return Response(serializer.data)

    def put(self, request, pk):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        donor = self.get_object(pk)
        donor.delete()
        return Response()

class ReceipentList(APIView):
    def get(self, request):
        receipents = Receipent.objects.all()
        serializer = ReceipentSerializer(receipents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceipentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReceipentDetail(APIView):
    def get_object(self, pk):
        try:
            return Receipent.objects.get(pk=pk)
        except Receipent.DoesNotExist:
            return Response()

    def get(self, request, pk):
        receipent = self.get_object(pk)
        serializer = ReceipentSerializer(receipent)
        return Response(serializer.data)

    def put(self, request, pk):
        receipent = self.get_object(pk)
        serializer = ReceipentSerializer(receipent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        receipent = self.get_object(pk)
        receipent.delete()
        return Response()

class BloodBankList(APIView):
    def get(self, request):
        bloodbanks = BloodBank.objects.all()
        serializer = BloodBankSerializer(bloodbanks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BloodBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BloodBankDetail(APIView):
    def get_object(self, pk):
        try:
            return BloodBank.objects.get(pk=pk)
        except BloodBank.DoesNotExist:
            return Response()

    def get(self, request, pk):
        bloodbank = self.get_object(pk)
        serializer = BloodBankSerializer(bloodbank)
        return Response(serializer.data)

    def put(self, request, pk):
        bloodbank = self.get_object(pk)
        serializer = BloodBankSerializer(bloodbank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        bloodbank = self.get_object(pk)
        bloodbank.delete()
        return Response()