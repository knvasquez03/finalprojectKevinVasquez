# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
