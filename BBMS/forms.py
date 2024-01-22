# accounts/forms.py
from django import forms
from .models import *

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(), required=True)

class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'last name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password'})
    )