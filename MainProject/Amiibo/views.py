# To understand the program flow a little better, this is how we got here (I think):
# >>> MainProject.urls reads the URL
# >>> MainProject.urls sees amiibo/ at end of URL so gos to Amiibo.url
# >>> Amiibo.urls reads the URL
# >>> Amiibo.urls, depending on what it reads, one of the functions below is run.

from django.shortcuts import render, get_object_or_404
from .forms import AmiiboFigureForm, APIFilterForm, newsFilterForm
from .models import AmiiboFigure
import requests             # To access the API
import json
import math
import re
import random
from bs4 import BeautifulSoup
from datetime import datetime

# Called when Amiibo/urls.py sees  ''  at the end of the URL
# Returns the HTML file amiibo_home.html
def amiibo_home(request):
    return render(request, 'Amiibo/amiibo_home.html')

# Called when Amiibo/urls.py sees  'yourcollection'  at the end of the URL
# Returns the HTML file amiibo_db.html which shows the contents of the database.
def amiibo_db(request):
    # NEW FEATURE: When user clicks "Add Amiibo" on the addAmiibo page they are taken to their collection.
    # When the ModelForm is POSTed here, save it in the database.
    # REMOVE THIS LATER.  FEATURE CAN BE ACCOMPLISHED WITHOUT NEEDING TO GET THE FORM HERE.
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


# Shows the page used to edit the information for an amiibo.
def amiibo_edit(request, pk):
    print("\n\n\n\n\n\nEntered the edit View!\n\n\n\n\n\n")

    pk = int(pk)

    # Get the selected amiibo using the primary key.
    amiibo = get_object_or_404(AmiiboFigure, pk=pk)

    # If there was a POST sent here, update the amiibo information
    if request.method == "POST":
        # Initialize the form with the Amiibo's current information
        form = AmiiboFigureForm(request.POST, instance=amiibo)

        # IF the form is valid, save it to the database and return to your collection
        if form.is_valid():
            # Once the form is submitted and valid, overwrite the information in amiibo and update the DB.
            amiibo = form.save(commit=False)
            amiibo.save()

            amiibos = AmiiboFigure.AmiiboFigurines.all()

            context = {
                'amiibos': amiibos,
                'AmiiboUpdateMessage': "{} was edited!".format(amiibo),
            }

            return render(request, 'Amiibo/amiibo_db.html', context)
    else:
        form = AmiiboFigureForm(instance=amiibo)

    context = {
        'form': form,
        'amiibo': amiibo,
    }

    return render(request, 'Amiibo/amiibo_db-details-edit.html', context)


# Deletes the selected Amiibo then returns back to your collection.
def amiibo_delete(request, pk):
    pk = int(pk)

    amiibo = get_object_or_404(AmiiboFigure, pk=pk)
    amiibo.delete()

    amiibos = AmiiboFigure.AmiiboFigurines.all()  # Put all of the variables in the db into the variable

    context = {
        'amiibos': amiibos,
        'AmiiboDeleteMessage': "{} has been removed from your collection".format(amiibo),
    }

    return render(request, 'Amiibo/amiibo_db.html', context)


# Called when Amiibo/urls.py sees  'amiibolist'  at the end of the URL
# Returns the HTML file amiibo_api.html
# API: https://www.amiiboapi.com/docs/
def amiibo_api(request):
    # The values I'll be getting from the API.  I may add more later | The default values when you visit the page.
    randomDefaultCharacters = ['Pikachu', 'King Dedede', 'Jigglypuff', 'Charizard']
    character = random.choice(randomDefaultCharacters)
    gameseries = ''
    dateChoice = 'Before'   # Not in API
    date = ''

    filterDict = {
        'character': character,
        'gameseries': gameseries,
    }

    str_api = "https://www.amiiboapi.com/api/amiibo/?"

    form = APIFilterForm(request.POST or None)
    if form.is_valid():
        filterDict.update({'character': request.POST.get('characterName').strip()})
        filterDict.update({'gameseries': request.POST.get('gameSeries').strip()})
        dateChoice = request.POST.get('dateChoices')
        date = request.POST.get('date')
        # form = APIFilterForm()

    # Using params attribute is very inconsistent so I'm doing the searches manually.
    # pt("Values before if statements:\n>>> Character: {}\n>>> Game Series: {}".format(character, gameSeries))
    # Determines which fields where blank and modifies the query accordingly.
    for key, val in filterDict.items():
        # pt("Key: {} | Value: {}".format(key, val))
        # Change the filter only if the user typed something into the fields.
        if val is not None and not val == '':
            str_api += "{}={}&".format(key, val)

        # if val is None:
        #     val == ''
        # if not val == '':
        #     str_api += "{}={}&".format(key, val)

    # Don't connect if there is no applied filter (there would be WAY too many images)
    if str_api == "https://www.amiiboapi.com/api/amiibo/?":
        statusCode = 404
    else:
        response = requests.get(str_api)
        statusCode = response.status_code  # Gives you information on the connection based on the number returned.

    pt("Status Code: {}".format(statusCode))

    # I we connected to the API, get all of the Amiibos and send them to the page.
    if statusCode == 200:
        amiiboData = response.json()['amiibo']        # Get the JavaScript Object Notation (JSON) from the API

        # REMOVE ME!!! - Testing if the regex works
        if re.match('(\d{4})-(\d{2})-(\d{2})', date):
            pt("The regex works!!!!!!")
        else:
            pt("Failed regex...")

        # Filtering by date
        if (not (date is None or date == '')) and re.match('(\d{4})-(\d{2})-(\d{2})', date):
            pt("Looking for Amiibos {} {}".format(dateChoice, date))
            if dateChoice == 'Before':
                # If not reversed, items could get skipped.
                # Check for dates NOT before the release date and remove them.
                for amiibo in reversed(amiiboData):
                    amiiboDate = amiibo['release']['na']
                    if amiiboDate >= date:
                        # pt(">>> Removed {} with a date of {}".format(amiibo['character'], amiiboDate))
                        amiiboData.remove(amiibo)

            elif dateChoice == 'On':
                # If not reversed, items could get skipped.
                # Check for dates NOT on the release date and remove them.
                for amiibo in reversed(amiiboData):
                    amiiboDate = amiibo['release']['na']
                    if not amiiboDate == date:
                        # pt(">>> Removed {} with a date of {}".format(amiibo['character'], amiiboDate))
                        amiiboData.remove(amiibo)

            elif dateChoice == "After":
                # If not reversed, items could get skipped.
                # Check for dates NOT after the release date and remove them.
                for amiibo in reversed(amiiboData):
                    amiiboDate = amiibo['release']['na']
                    if amiiboDate <= date:
                        # pt(">>> Removed {} with a date of {}".format(amiibo['character'], amiiboDate))
                        amiiboData.remove(amiibo)
        else:
            pt("Not filtering based on date")

        print(json.dumps(amiiboData, sort_keys=True, indent=4))

        # Eventually, I want only a certain number of Amiibos on the page so that the app doesn't annihilate
        # someones bandwidth if they don't filter out enough Amiibos.
        amiibosPerPage = 10
        numberOfAmiibos = len(amiiboData)
        pages = math.ceil((numberOfAmiibos / amiibosPerPage))

        # This is the JSON response printed to the console.
        # print(json.dumps(amiiboData, sort_keys=True, indent=4))     # Makes the data easier to see.

        # I'm getting the value for image, name, character, game series, release, and type.
        context = {
            'form': form,
            'amiiboData': amiiboData,
            'pages': pages,  # I only want 10 amiibos per page.
        }

        if len(amiiboData) == 0:
            context['message'] = "We found nothing based on your constraints..."
    else:
        context = {
            'form': form,
            'message': "That's a 404!! Maybe there was a typo...",
        }

    return render(request, 'Amiibo/amiibo_api.html', context)

# Called when Amiibo/urls.py sees  'nintendonews'  at the end of the URL
# Returns the HTML file amiibo_news.html
def amiibo_news(request):
    # DEFAULT FORM VALUES
    search = ''
    time_frame = 'Newest'
    numberOfArticles = 10

    form = newsFilterForm(request.POST or None)
    if form.is_valid():
        search = request.POST.get("search")
        time_frame = request.POST.get("time_frame")
        numOfArticles = request.POST.get("numOfArticles")
        if numOfArticles is None or numOfArticles == '':
            numOfArticles = 10;

    # Connects to the web page and returns all of the articles and the connection. | Called when "Newest" is selected
    def getLatestNews(numOfArt):
        # Connects to the website and creates the beautiful soup.
        connection = requests.get("https://nintendonews.com/")  # Website I'm scraping from

        # The Beautiful Soup HTML parser.  This will get the HTML from the connection above.
        soup = BeautifulSoup(connection.content, 'html.parser', from_encoding="utf-8")

        # soup.children gives a list generator.  Making it into a list that looks like ['html', '\n', HTML]
        # List where the head is index 1 and body is index 3.  These are the children of <html>
        html = list(soup.children)[2]

        return html.find_all("div", class_="item has-target", limit=int(numOfArt)), connection

    # Getting the date and time based on user's computer
    systemDate = datetime.now().strftime("%Y%m%d")
    systemTime = datetime.now().strftime("%H%M%S")




    # Filtering by time_frame
    articlesFound = 0
    if time_frame == "Newest":
        contentDiv, page = getLatestNews(numOfArticles)
    elif time_frame == "Yesterday":
        pt()
    elif time_frame == "Last Week":
        pt()
    else:   # If somehow it's not one of these, assume "Newest"
        contentDiv, page = getLatestNews(numOfArticles)
    # contentDiv is a ResultSet - it's a list of div tags.  contentDiv: [div, div, div, ... , div]




    articles = []
    if page.status_code == 200:

        for article in contentDiv:
            age = article.find("p", class_="date").get_text().replace("&bullet", "|")
            title = article.find("h2", class_="heading").get_text()
            summary = article.find("p", class_="summary").get_text()
            link = article.find("a").get('href')

            # Filtering by search
            if search is None or search == '':
                articles.append({'age': age, 'title': title, 'summary': summary, 'link': link})
                # pt("Empty search: IGNORE SEARCH")
            else:
                if re.search(search, summary, re.IGNORECASE) is not None:
                    # pt("Search Match!!! Adding!!!")
                    articles.append({'age': age, 'title': title, 'summary': summary, 'link': link})
                else:
                    pt("Didn't match anything...")
    else:
        articles.append({'age': "", 'title': "We can't connect to the server!", 'summary': "Sorry...", 'link': ""})

    context = {
        'articles': articles,
        'form': form,
    }
    return render(request, 'Amiibo/amiibo_news.html', context)

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

# Just a quick way to see my prints in the console
def pt(s):
    print(">>> {}\n".format(s))

# Easy way to see a list in the console:
def viewList(lst, lstTitle = None):
    position = 0

    # If no title is specified, ignore it and continue
    if lstTitle is None:
        print("\n[\n")
    else:
        print("\n{}:\n[\n".format(lstTitle))

    # print all of the elements in the list and be aware of \n
    for element in lst:
        if element == '\n':
            print("\t({}) >>> {}\n".format(position, '\\n'))
        else:
            print("\t({}) >>> {}\n".format(position, element))
        position += 1

    print("]\n{}".format(type(lst)))