from django.contrib import admin
from django.urls import path
from .views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('index_about',index_about,name='index_about'),
    
    path('donor/',donor,name='donor'),
    path('bloodrequest/',bloodrequest,name='bloodrequest'),
    path('register/',register, name='register'),
    path('register/auth/', AuthView.as_view(), name='auth'),
    path('login/',user_login, name='login'),
    
    path('logout/', logout, name='logout'),
    
    path('admin/logout/', custom_logout, name='custom_logout'),
    
    path('dashboard/',dashboard,name='dashboard'),
    path('landing_page/',landing_page,name='landing_page'),
    path('index/',index,name='index'),

    
    path('donors/<pk>/delete',delete_donor),
    path('receipent/<pk>/delete',delete_receipent),
    
    path('donor/<pk>/edit_donor',edit_donor),
    path('receipent/<pk>/edit_receipent',edit_receipent),

     
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



     
     

