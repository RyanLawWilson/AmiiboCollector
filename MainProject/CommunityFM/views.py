from django.shortcuts import render


# Function that renders the home page
def radioHome(request):
    return render(request, 'CommunityFM/fm_home.html')



# Create your views here.
