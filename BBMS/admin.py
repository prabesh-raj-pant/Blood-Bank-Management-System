from django.contrib import admin
from .models import Donor, Receipent, BloodBank

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('Donor_Name', 'Donor_Age', 'Donor_BloodType')  # Use '=' instead of ':' to define list_display
    search_fields = ('Donor_BloodType',)  # Use 'fields' instead of 'field' and make it a tuple

@admin.register(Receipent)
class ReceipentAdmin(admin.ModelAdmin):
    list_display = ('Receipent_Name', 'Receipent_Age', 'Receipent_BloodType')
    search_fields = ('Receipent_BloodType',)

@admin.register(BloodBank)
class BloodBankAdmin(admin.ModelAdmin):
    pass
