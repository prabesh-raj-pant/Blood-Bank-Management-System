from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Donor(models.Model):
    Donor_Name = models.CharField(max_length=100)
    Donor_Age = models.IntegerField(default=10)
    Donor_Address=models.CharField(max_length=100)
    Donor_BloodType = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Donor_Email=models.CharField(max_length=100)
    Donor_Phone=models.BigIntegerField(default=10)
    Donor_DateTime = models.DateTimeField(auto_now_add=True)

    

class Receipent(models.Model):
    Receipent_Name = models.CharField(max_length=100)
    Receipent_Age = models.IntegerField(default=10)
    Receipent_BloodType = models.CharField(max_length=50)
    Receipent_Address = models.CharField(max_length=50)
    Receipent_Email = models.CharField(max_length=50)
    Receipent_Phone= models.BigIntegerField(default=50)
    Receipent_Hospital= models.CharField(max_length=50)
    Receipent_DateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Receipent_Name

class BloodBank(models.Model):
    BloodBank_Order = models.CharField(max_length=100)
    BloodBank_Bloodtype = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.BloodBank_Order

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    
