import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import surfType
from .forms import BoardForm
from django.utils import timezone
import requests
#from api_service import *



#View function that renders the home page - no context needed
def WaveHome(request):
    return render(request, "WaveWatch/wavewatch_home.html")

def index(request):
    get_surfinfo = surfType.surfTypes.all()      #Gets all the current info from the database
    context = {'surfdata': get_surfinfo}      #Creates a dictionary object of all the info for the template
    return render(request, 'WaveWatch/wavewatch_index.html', context)

def add_surfInfo(request):
    form = BoardForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/jersey to the database
        return redirect('listSurfType')                #Redirects to the index page, which is named 'waves' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = BoardForm()                     #Creates a new blank form
    return render(request, 'WaveWatch/wavewatch_create.html', {'form':form})

def details_surfInfo(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    surfID = get_object_or_404(surfType, pk=pk)   #Gets single instance of the data from the database
    context={'surfID':surfID}                    #Creates dictionary object to pass the object
    return render(request,'WaveWatch/wavewatch_details.html', context)

def update_surfInfo(request, pk):
    surfID = get_object_or_404(surfType, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=surfID)
        if form.is_valid():
            surfID = form.save(commit=False)
            surfID.author = request.user
            surfID.published_date = timezone.now()
            surfID.save()
            return redirect('surfInfoDetails', pk=surfID.pk)
    else:
        form = BoardForm(instance=surfID)
    return render(request, 'WaveWatch/wavewatch_update.html', {'form': form})

def delete_surfInfo(request, pk):
    surfID = get_object_or_404(surfType, pk=pk)
    #POST request
    if request.method == "POST":
        #confirming delete
        surfID.delete()
        return redirect('WaveWatch/wavewatch_index.html')
    context = {"surfID": surfID}
    return render(request, "WaveWatch/wavewatch_delete", context)

"""
path('', views.WaveHome, name='waves'),
path('Collection/', views.index, name='listSurfType'),  # index of jerseys
path('AddTo/', views.add_surfInfo, name='addSurfInfo'),  # index of jerseys
path('Collection/<int:pk>/Details/', views.details_surfInfo, name='surfInfoDetails'),
path('Collection/<int:pk>/Update/', views.update_surfInfo, name='updateSurfInfo')
path('Collection/<int:pk>/Delete/', views.delete_surfInfo, name='deleteSurfInfo')

class BoardForm(ModelForm):
    class Meta:
        model = surfType
        fields = '__all__'

class surfType(models.Model):
    locale = models.CharField(max_length=40)
    country = models.CharField(max_length=30, blank=True)
    board_type = models.CharField(max_length=20, choices=BOARD_TYPES)
    board_length = models.CharField(max_length=20, choices=BOARD_LENGTHS)

    surfTypes = models.Manager()

    def __str__(self):
        return self.locale
"""