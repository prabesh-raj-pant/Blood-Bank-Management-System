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
    path('register/',register, name='register'),
    path('register/auth/', AuthView.as_view(), name='auth'),
    path('login/',user_login, name='login'),
]
