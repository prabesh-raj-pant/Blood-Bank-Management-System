# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from .serializer import *
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

def dashboard(request):
    return render(request,'dashboard.html')

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
            return redirect('dashboard')
        else:
            return render(request, 'register/auth.html', {'error_message': 'Invalid login credentials'})

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

