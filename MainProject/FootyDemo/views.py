import datetime                     #used for passing dates in easy to display format
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jersey          #import the class of Jersey to be able to use object definition
from .forms import JerseyForm       #import the Jersey Form to be able to create and save
from .api_service import *          #imports the functions from the API Service module created
from django.utils import timezone   #used for converting time from UTC to users time zone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping

# Create your views here.


#View function that renders the home page - no context needed
def home(request):
    return render(request, 'FootyDemo/footy_home.html')

#View function that controls the main index page - list of jerseys
def index(request):
    get_jerseys = Jersey.Jerseys.all()      #Gets all the current jerseys from the database
    context = {'jerseys': get_jerseys}      #Creates a dictionary object of all the jerseys for the template
    return render(request, 'FootyDemo/footy_index.html', context)


#View function to add a new jersey to the database
def add_jersey(request):
    form = JerseyForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/jersey to the database
        return redirect('listJerseys')                #Redirects to the index page, which is named 'footy' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = JerseyForm()                     #Creates a new blank form
    return render(request, 'FootyDemo/footy_create.html', {'form':form})


#View function to look up the details of a jersey
def details_jersey(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    jersey = get_object_or_404(Jersey, pk=pk)   #Gets single instance of the jersey from the database
    context={'jersey':jersey}                   #Creates dictionary object to pass the jersey object
    return render(request,'FootyDemo/footy_details.html', context)


#View function for the main API page with dropdowns
def api_response(request):
    context = {'world': get_areas()}            #Creates a dictionary item of all the world areas
    if request.method == 'POST':                #This block will handle all post backs from the forms
        print(request.POST)                     #This was used for debugging purposes
        if 'league' in request.POST:            #Checks for a league item, knows we're in the third dropdown
            league_id = request.POST['league']  #Gets the value of league from the dropdown menu, an element of the Post dictionary
            matches_page = '../{}/Matches'.format(league_id)    #Dynamically sets the redirect page
            return redirect(matches_page)       #Sends user to matches page, url contains the code the view function needs
        elif 'childArea' in request.POST:         #If there isn't a league, checks for value from the second dropdown
            if request.POST['submit'] == 'noFilter':    #If the user pressed the no filter button
                child = request.POST['parentArea']      #Sets the league dropdown to all of the options for the parent
            else:                                       #If user filtered by country
                child = request.POST['childArea']       #Sets the league dropdown to the options for child
            leagues = get_leagues(child)                #Gets the leagues for the specified area
            context.update({'leagues': leagues, 'childArea':request.POST['childArea']})     #Adds information to context to populate dropdowns

        parent = request.POST['parentArea']     #Gets the value of the parent area
        add_parents = {'parents': get_children(parent)}     #Creates a dictionary item of the parent areas
        context.update(add_parents)             #Adds the parents to the context item

    return render(request, 'FootyDemo/footy_api.html', context)


#View function for the matches page - uses the url to pass in the code for the specific league/competition
def matches(request, code):
    league_dictionary= get_matches(code)        #Gets the Json response dictionary for that league
    context={'matches': []}                     #Creates a dictionary item with a key, and a blank array for the value
    for match in league_dictionary['matches']:  #Iterates through the matches within the JSON response
        local_date = convert_to_localtime(match['utcDate'])   #Gets utcDate and converts it to local time, function below
        game= {'date': local_date,              #Creates a new dictionary item, temporarily called game, sets date to local date
               'winner': match['score']['winner'],      #Sets winner to value in Json, either home team or away team
               'score_home': match['score']['fullTime']['homeTeam'],    #Sets home score to home team score
               'score_away': match['score']['fullTime']['awayTeam'],    #Sets away score to away team score
               'home_team': match['homeTeam']['name'],                  #Sets home team to the name of the home team
               'away_team': match['awayTeam']['name']}                  #Sets away team to name of the away team
        print(game)                                     #Used for debugging, prints the game object to the terminal
        context['matches'].append(game)                 #Adds the game item to the array in the dictionary, then iterates through next item
    context.update({'local_tz':timezone.get_current_timezone_name()}) #Adds the local timezone to the context object

    return render(request, 'FootyDemo/footy_matches.html', context) #Sends completed dictionary of matches and timezone to template


#View function for data scraping the MLS website for current news stories
def mls_news(request):
    source = requests.get("https://www.mlssoccer.com/news")     #Get MLSSoccer.com/news as an html document
    print(source.status_code)                   #Used for debugging to ensure a 'success' code of 200
    soup = BS(source.content, 'html.parser')    #Initial processing of the html by beautiful soup, soup is now a navigatable object
    nodes = soup.find_all(class_="node-title")  # Search for divs with class node-title
    articles = []                               #Create blank array to add articles to
    for node in nodes:                          #Iterates through all the objects with class of node-title
        title = node.find('a').get_text()       #Sets title equal to the text of the a tag
        link = node.find('a').get('href')       #Sets link equal to the href of the a tag
        timestamp = node.find_next_siblings(class_="timestamp")[0].get_text()   #Uses class and sibling relationship to get the timestamp
        url = "https://www.mlssoccer.com" + link    #Modifies the link to a full url, since the links were relative
        article={'title':title, 'url': url, 'date': timestamp}  #Creates and article object dictionary with needed elements
        articles.append(article)            #Adds article dictionary item to the array before iterating through next node
    context={'articles': articles}          #Creates a dictionary element for the articles to pass to the template
    return render(request, 'FootyDemo/mls_news.html', context)


#Function used to convert utc time into local time, pulled from Stack Overflow
def convert_to_localtime(utctime):
    localdatetime = datetime.datetime.strptime(utctime, '%Y-%m-%dT%H:%M:%SZ')   #Uses strptime to pull out time elements, this must match the format being sent
    return localdatetime
