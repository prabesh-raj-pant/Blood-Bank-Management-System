from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Donor(models.Model):
 
    Donor_Name=models.CharField(max_length=100)
    Donor_Age=models.IntegerField(default=10)
    Donor_BloodType=models.CharField(max_length=50)
    
    
    
    
