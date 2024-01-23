
from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/', signUp, name='signup'),
    path('login/', login, name='login'),
    path('index/',index,name='index'),
    path('bbsm',include('bbsm.urls')),
]
