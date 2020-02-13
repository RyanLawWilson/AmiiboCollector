from django.shortcuts import render


#View function that renders the home page - no context needed
def home(request):
    return render(request, 'wave/WaveWatch.html')

