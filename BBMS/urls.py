
from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/', signUp, name='signup'),
    path('login/', login, name='login'),
    path('index/',index,name='index'),
    
    

    path('donors/', DonorList.as_view(), name='donor-list'),
    path('donors/<int:pk>/', DonorDetail.as_view(), name='donor-detail'),
    
    path('receipents/', ReceipentList.as_view(), name='receipent-list'),
    path('receipents/<int:pk>/', ReceipentDetail.as_view(), name='receipent-detail'),


    path('bloodbanks/', BloodBankList.as_view(), name='bloodbank-list'),
    path('bloodbanks/<int:pk>/', BloodBankDetail.as_view(), name='bloodbank-detail'),
    
]


    
     
     
     

