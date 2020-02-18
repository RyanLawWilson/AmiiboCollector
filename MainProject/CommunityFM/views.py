from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StationForm
from .models import Station


# Function that renders the home page
def radioHome(request):
    return render(request, 'CommunityFM/fm_home.html')

#Function to add a new station to the database
def add_station(request):
    form = StationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('addStation')
    else:
        print(form.errors)
        form = StationForm()
    return render(request, "CommunityFM/fm_create.html", {"form": form})




# Create your views here.
