from django.shortcuts import render


# Function that renders the home page
def bookBagHome(request):
    return render(request, 'BookBag/bookBag_home.html')
