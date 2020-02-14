# To understand the program flow a little better, this is how we got here (I think):
# >>> MainProject.urls reads the URL
# >>> MainProject.urls sees amiibo/ at end of URL so gos to Amiibo.url
# >>> Amiibo.urls reads the URL
# >>> Amiibo.urls, depending on what it reads, one of the functions below is run.

from django.shortcuts import render, get_object_or_404
from .forms import AmiiboFigureForm
from .models import AmiiboFigure

# Called when Amiibo/urls.py sees  ''  at the end of the URL
# Returns the HTML file amiibo_home.html
def amiibo_home(request):
    return render(request, 'Amiibo/amiibo_home.html')

# Called when Amiibo/urls.py sees  'yourcollection'  at the end of the URL
# Returns the HTML file amiibo_db.html which shows the contents of the database.
def amiibo_db(request):
    # NEW FEATURE: When user clicks "Add Amiibo" on the addAmiibo page they are taken to their collection.
    # When the ModelForm is POSTed here, save it in the database.
    form = AmiiboFigureForm(request.POST or None)
    if form.is_valid():
        form.save()

    amiibos = AmiiboFigure.AmiiboFigurines.all()        # Put all of the variables in the db into the variable

    context = {
        'amiibos': amiibos,
    }

    return render(request, 'Amiibo/amiibo_db.html', context)

# Called when Amiibo/urls.py sees  'yourcollection/details'  at the end of the URL
# Gets the AmiiboFigure instance that was clicked and sends it to details page.
# Returns the HTML file amiibo_db-details.html
def amiibo_details(request, pk):
    # I'll determine what amiibo to show details of based on its primary key.
    pk = int(pk)    # Make sure it's an integer.
    amiibo = get_object_or_404(AmiiboFigure, pk=pk)

    context = {
        'amiibo': amiibo
    }

    # When the primary key is passed to this function, the corresponding amiibo is retrieved and
    # sent to amiibo_db-details.html.  Now we have to figure out how the primary key sent here and
    # what the amiibo does once it gets to the details page.
    # TLDR: We get pk, we get amiibo using pk, we send amiibo to details page.
    #       How do we send pk here?
    #       Utilize amiibo in details page.
    return render(request, 'Amiibo/amiibo_db-details.html', context)

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
    if form.is_valid():
        form.save()
        form = AmiiboFigureForm()   # Makes the contents of the form refresh when the user add Amiibo save.

    # Make a dictionary to send to the page that will be rendered
    context = {
        'form': form
    }

    # We are rendering the addAmiibo page with the ModelForm that we specified in forms.py
    return render(request, 'Amiibo/amiibo_db-addAmiibo.html', context)


# Returns to the collection when you click the submit button on the addAmiibo page.
def amiiboAdded(request, message):
    message = ""

    context = {
        'message': message
    }

    return render(request, 'Amiibo/amiibo_db.html', context)