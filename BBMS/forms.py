from django import forms
from .models import Profile
from .models import Donor, Receipent

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['Donor_Name', 'Donor_Age', 'Donor_Address', 'Donor_BloodType', 'Donor_Phone']

class ReceipentForm(forms.ModelForm):
    class Meta:
        model = Receipent
        fields = ['Receipent_Name', 'Receipent_Age', 'Receipent_BloodType', 'Receipent_Address', 'Receipent_Email', 'Receipent_Phone', 'Receipent_Hospital']