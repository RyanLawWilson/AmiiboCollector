from django.shortcuts import render


#View function that renders the home page - no context needed
def WaveHome(request):
    return render(request, "WaveWatch/wavewatch_home.html")


# Create your views here.
