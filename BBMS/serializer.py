from rest_framework import serializers
from .models import *

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['Donor_Name', 'Donor_Age', 'Donor_BloodType', 'user']
        list_display_links = ('Donor_Name', 'Donor_Age', 'Donor_BloodType', 'user')
    
class ReceipentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipent
        fields = ['Receipent_Name', 'Receipent_Age', 'Receipent_BloodType', 'user']
        list_display_links = ('Receipent_Name', 'Receipent_Age', 'Receipent_BloodType', 'user')

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = ['BloodBank_Order', 'BloodBank_Bloodtype', 'user']



    