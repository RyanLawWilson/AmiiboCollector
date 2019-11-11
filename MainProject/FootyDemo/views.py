from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'FootyDemo/footy_index.html')