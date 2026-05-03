# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.contrib import admin
from .models import Client, TimeEntry


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hourly_rate', 'user')
    search_fields = ('name', 'email')
    list_filter = ('user',)


@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('client', 'description', 'hours_worked', 'date_worked', 'user')
    search_fields = ('description', 'client__name')
    list_filter = ('date_worked', 'client', 'user')