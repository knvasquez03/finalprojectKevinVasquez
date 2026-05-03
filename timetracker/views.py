# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Client, TimeEntry
from .forms import ClientForm, TimeEntryForm, RegisterForm
from decimal import Decimal
import requests


def home(request):
    return render(request, 'timetracker/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    entries = TimeEntry.objects.filter(user=request.user).order_by('-date_worked')

    current_time = "Time unavailable"

    try:
        response = requests.get(
            "https://worldtimeapi.org/api/timezone/America/Chicago",
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            current_time = data.get("datetime", "Time unavailable")
    except requests.RequestException:
        current_time = "Time unavailable"

    return render(request, 'timetracker/dashboard.html', {
        'entries': entries,
        'current_time': current_time
    })

@login_required
def clients(request):
    clients_list = Client.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('clients')
    else:
        form = ClientForm()

    return render(request, 'timetracker/clients.html', {
        'clients': clients_list,
        'form': form
    })


@login_required
def add_entry(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        form.fields['client'].queryset = Client.objects.filter(user=request.user)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = TimeEntryForm()
        form.fields['client'].queryset = Client.objects.filter(user=request.user)

    return render(request, 'timetracker/add_entry.html', {'form': form})

@login_required
def summary(request):
    entries = TimeEntry.objects.filter(user=request.user)

    total_hours = sum(entry.hours_worked for entry in entries)
    total_earnings = sum(entry.total_amount() for entry in entries)

    return render(request, 'timetracker/summary.html', {
        'total_hours': total_hours,
        'total_earnings': total_earnings,
        'entry_count': entries.count()
    })


@login_required
def profile(request):
    client_count = Client.objects.filter(user=request.user).count()
    entry_count = TimeEntry.objects.filter(user=request.user).count()

    return render(request, 'timetracker/profile.html', {
        'client_count': client_count,
        'entry_count': entry_count
    })
