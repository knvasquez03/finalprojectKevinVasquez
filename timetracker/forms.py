# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client, TimeEntry


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'hourly_rate']


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['client', 'description', 'hours_worked', 'date_worked']
        widgets = {
            'date_worked': forms.DateInput(attrs={'type': 'date'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']