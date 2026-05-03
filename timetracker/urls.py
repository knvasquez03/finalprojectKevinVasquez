# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', views.clients, name='clients'),
    path('add-entry/', views.add_entry, name='add_entry'),
    path('summary/', views.summary, name='summary'),
    path('profile/', views.profile, name='profile'),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]