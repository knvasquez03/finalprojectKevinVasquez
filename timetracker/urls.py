# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', views.clients, name='clients'),
    path('add-entry/', views.add_entry, name='add_entry'),
]