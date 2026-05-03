# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Final Project

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TimeEntry(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    date_worked = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return self.hours_worked * self.client.hourly_rate

    def __str__(self):
        return f"{self.client.name} - {self.description}"