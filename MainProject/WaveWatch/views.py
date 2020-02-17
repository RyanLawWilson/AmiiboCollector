from django.shortcuts import render, redirect, get_object_or_404
from .models import surfType
from .forms import BoardForm
#from api_service import *



#View function that renders the home page - no context needed
def WaveHome(request):
    return render(request, "WaveWatch/wavewatch_home.html")

def index(request):
    get_surfinfo = surfType.surfTypes.all()      #Gets all the current jerseys from the database
    context = {'surfdata': get_surfinfo}      #Creates a dictionary object of all the jerseys for the template
    return render(request, 'WaveWatch/wavewatch_index.html', context)

def add_surfInfo(request):
    form = BoardForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/jersey to the database
        return redirect('listSurfType')                #Redirects to the index page, which is named 'footy' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = BoardForm()                     #Creates a new blank form
    return render(request, 'WaveWatch/wavewatch_create.html', {'form':form})

def details_surfInfo(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    surfID = get_object_or_404(surfType, pk=pk)   #Gets single instance of the jersey from the database
    context={'surfID':surfID}                   #Creates dictionary object to pass the jersey object
    return render(request,'WaveWatch/wavewatch_details.html', context)

#def api_response(request):

