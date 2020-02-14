# To understand the program flow a little better, this is how we got here (I think):
# >>> MainProject.urls reads the URL
# >>> MainProject.urls sees amiibo/ at end of URL so gos to Amiibo.url
# >>> Amiibo.urls reads the URL
# >>> Amiibo.urls, depending on what it reads, one of the functions below is run.

from django.shortcuts import render
from .forms import AmiiboFigureForm
from .models import AmiiboFigure

# Called when Amiibo/urls.py sees  ''  at the end of the URL
# Returns the HTML file amiibo_home.html
def amiibo_home(request):
    return render(request, 'Amiibo/amiibo_home.html')

# Called when Amiibo/urls.py sees  'yourcollection'  at the end of the URL
# Returns the HTML file amiibo_db.html which shows the contents of the database.
def amiibo_db(request):
    amiibos = AmiiboFigure.AmiiboFigurines.all()        # Put all of the variables in the db into the variable

    context = {
        'amiibos': amiibos,
    }

    return render(request, 'Amiibo/amiibo_db.html', context)

# Called when Amiibo/urls.py sees  'amiibolist'  at the end of the URL
# Returns the HTML file amiibo_api.html
def amiibo_api(request):
    return render(request, 'Amiibo/amiibo_api.html')

# Called when Amiibo/urls.py sees  'nintendonews'  at the end of the URL
# Returns the HTML file amiibo_news.html
def amiibo_news(request):
    return render(request, 'Amiibo/amiibo_news.html')

# Called when Amiibo/urls.py sees  'amiibo/addAmiibo'  at the end of the URL
# Returns the HTML file amiibo_db-addAmiibo.html
# I followed this video: https://www.youtube.com/watch?v=6oOHlcHkX2U
def addAmiibo(request):
    form = AmiiboFigureForm(request.POST or None)     # The form for the database is going to be on this page.
    print(form)
    if form.is_valid():
        form.save()
        form = AmiiboFigureForm()   # Makes the contents of the form refresh when the user clicks save.

    # Make a dictionary to send to the page that will be rendered
    context = {
        'form': form
    }

    # We are rendering the addAmiibo page with the ModelForm that we specified in forms.py
    return render(request, 'Amiibo/amiibo_db-addAmiibo.html', context)