from django.views import View
from django.contrib import admin
from django.urls import path
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
]
