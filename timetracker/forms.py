# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

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