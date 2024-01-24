# views.py

from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

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

