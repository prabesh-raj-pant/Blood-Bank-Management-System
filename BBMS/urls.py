from django.views import View
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('donor/',donor,name='donor'),
    path('bloodrequest/',bloodrequest,name='bloodrequest'),
    path('register/',register, name='register'),
    path('register/auth/', AuthView.as_view(), name='auth'),
    path('login/',user_login, name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('index/',index,name='index'),
    path('donors/', DonorList.as_view(), name='donor-list'),
    path('donors/<int:pk>/', DonorDetail.as_view(), name='donor-detail'),
    
    path('receipents/', ReceipentList.as_view(), name='receipent-list'),
    path('receipents/<int:pk>/', ReceipentDetail.as_view(), name='receipent-detail'),


    path('bloodbanks/', BloodBankList.as_view(), name='bloodbank-list'),
    path('bloodbanks/<int:pk>/', BloodBankDetail.as_view(), name='bloodbank-detail'),
    
]


    
     
     
     

