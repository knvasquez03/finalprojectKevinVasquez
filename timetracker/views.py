# INF601 - Advanced Programming in Python
# Kevin Vasquez
# Final Project

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client, TimeEntry
from .forms import ClientForm, TimeEntryForm


def home(request):
    return render(request, 'timetracker/home.html')


@login_required
def dashboard(request):
    entries = TimeEntry.objects.filter(user=request.user).order_by('-date_worked')
    return render(request, 'timetracker/dashboard.html', {'entries': entries})


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
