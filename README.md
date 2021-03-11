<p align="center">
  <img src="./readme_resources/jigglypuff.png" width="100" alt="Jigglypuff Amiibo" />
  <img src="./readme_resources/title_text.png" />
  <img src="./readme_resources/king_dedede.png" width="100" alt="King Dedede Amiibo" />
</p>

For this project, I created a Django application. This app is themed around Amiibos.  You can create, edit, and delete your Amiibos and search for more Amiibos.  I use the [AmiiboApi](https://www.amiiboapi.com/) to search for all available Amiibos and display them on the page.  You can also look at general Nintendo news.  This page web scrapes [nintendonews.com](https://nintendonews.com/) for the latest Nintendo articles.

The database that I am using to store the Amiibos is a local database using **SQLite**.  To contact the API, I am using Python's **requests** module.  For web scraping, I am using **Beautiful Soup**.

<br>

*Table of Contents*
* **[CRUD Pages](#crud-pages)**
* **[AmiiboAPI](#amiibo-api)**
* **[Web Scraping](#web-scraping)**

<br>

<div align="center">


| **<div align="center">Technologies Used</div>** |
| --- |
| **Python • Django • API • JSON • SQL • HTML • CSS • JavaScript • Azure DevOps • Git • PyCharm** |

</div>

# <p align="center" name="crud-pages">CRUD Pages</p>

I created the CRUD functionality for my application (creating, updating, and deleting objects).  I created a model called AmmiboFigure to represent an individual Amiibo and I used a SQLite database to store objects.  There are 4 templates (pages) that I made for the CRUD functionality.

<p align="center">
    <img src="./readme_resources/homepage.gif" width="75%">
</p>

First, the **[Create page](./CRUD_pages.md#Create)**.  Here a user can save a new Amiibo to the database by filling out and submitting the form.  Next, the **[Index page](./CRUD_pages.md#Index)**.  This page shows the user the contents of the database (what AmiiboFigures are being stored).  From the Index page, the user can click on the details button for any of the Amiibos and see more information about that Amiibo on the **[Details page](./CRUD_pages.md#Details)**.  From the Details page, the user can either edit the Amiibo's properties from the **[Edit page](./CRUD_pages.md#Edit)** page or **[Delete](./CRUD_pages.md#Delete)** the Amiibo.  There isn't a page for deleting an Amiibo.  Instead, I opted for a confirmation modal.

<div align="center" name="crud-pages">

**You can find more detailed information about what I did for the CRUD pages [here](./CRUD_pages.md)**

</div>


# <p align="center" name="amiibo-api">AmiiboAPI</p>
An API that I used to complement my App was the [AmiiboAPI](https://www.amiiboapi.com/).  This API has nearly all of the Amiibos in existence as well as images to accompany them.  I use Python's `requests` module to contact the API and get data about Amiibos.

<p align="center">
    <img src="./readme_resources/API.gif" width="75%">
</p>

The code for getting information from the API is in my amiibo_api View method.  The first bit of code gets the filter information from the form so that we can query information from the API based on user input.  `filterDict` is a dictionary that contains the form information for the typed in character and game series.

```Python
str_api = "https://www.amiiboapi.com/api/amiibo/?"

form = APIFilterForm(request.POST or None)
if form.is_valid():
    filterDict.update({'character': request.POST.get('characterName').strip()})
    filterDict.update({'gameseries': request.POST.get('gameSeries').strip()})
    dateChoice = request.POST.get('dateChoices')
    date = request.POST.get('date')
```

Next, I add queries to the query string depending on what fields the user filled out.

```Python
# Using params attribute is very inconsistent so I'm doing the searches manually.
# pt("Values before if statements:\n>>> Character: {}\n>>> Game Series: {}".format(character, gameSeries))
# Determines which fields where blank and modifies the query accordingly.
for key, val in filterDict.items():
    # pt("Key: {} | Value: {}".format(key, val))
    # Change the filter only if the user typed something into the fields.
    if val is not None and not val == '':
        str_api += "{}={}&".format(key, val)
```

Once the string for the API is configured, I can contact the API to get Amiibos that match the query.  If the query didn't change, I make sure not to query the API because it will give me **ALL** of the Amiibos (including their images).  I use the requests module to contact the API and pass in my query string.

```Python
# Don't connect if there is no applied filter (there would be WAY too many images)
if str_api == "https://www.amiiboapi.com/api/amiibo/?":
    statusCode = 404
    response = None
else:
    response = requests.get(str_api)
    statusCode = response.status_code  # Gives you information on the connection based on the number returned.
```

There isn't an endpoint for the API that allows you to only select Amiibos Before, After, or Between certain times.  So I do that sorting myself after I get the JSON from the API.  After I get the JSON response from the API, I assign it to a variable called `amiiboData`.  If an Amiibos release date is not within the time frame specified in the form by the user, it is removed from `amiiboData`.

```Python
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
```

Once the Amiibos have been filtered, the Amiibos that didn't get deleted from the `amiiboData` list get sent to the template to be displayed on the page.

# <p align="center" name="web-scraping">Web Scraping</p>
The website that I am scraping from is [nintendonews.com](https://nintendonews.com/).  I am using the requests module and Beautiful Soup to scrape the page.  The user can enter text they want to search for, a particular timeframe, and how many articles that should be displayed.  The URL for the source article is found when scraping the nintendonews site and is displayed on the page so that users can go directly to the article without going through nintendonews.


<p align="center">
    <img src="./readme_resources/BS_Scrape.gif" width="75%">
</p>

I first initialize my Beautiful Soup object and identify the elements on that page that I want to scrape.  My App is built to search threw more that just the first page of the website if needed which is the reason for the `startingPage` variable.
```Python
page = requests.get(website + str(startingPage)) # Connects to the website and creates the beautiful soup.
soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8") # Gets the HTML from the page

# contentDiv is a ResultSet - it's a list of div tags.  contentDiv: [div, div, div, ... , div]
contentDiv = soup.find_all("div", class_="item has-target")
```

As I search through the articles on the website, I determine if they are in the timeframe that the user specified.  If they are not, the articles are not added to the list and are not sent down to the page.  The `time_frame` variable refers to the timeframe option that the user selected.  Options are "Today", "Yesterday", "A few days ago", and "Last Week".  The `systemTime` variable is just the current time.

```Python
# Define the time_frame filter - Determines if an articles is going to be added based on age.
def filterByTime_Frame(timePassed, timeUnit):
    # Get articles based on time_frame (Today, Yesterday, Last Week)
    if time_frame == "Today":
        # If the age of the article is in minutes, compare against system time to see if it came out yesterday.
        if re.match("mins?", timeUnit):
            # If the age of the article, in minutes, is longer than system time, it's yesterday
            return True if int(timePassed) * 100 < systemTime else False
        # If the age of the article is in hours, compare against system time to see if it came out yesterday.
        elif re.match("hours?", timeUnit):
            # If the age of the article, in hours, is longer than system time, it's yesterday
            return True if int(timePassed) * 10000 < systemTime else False
        # If the age of the article is in days, only pick the articles that are 1 day old.
        elif re.match("days?", timeUnit):
            return False
        # If the age of the article is represented by a date (article more than 7 days old), ignore it.
        else:
            return False
```

If there are any articles that fall in that timeframe (`time_frameFilterPassed` is **true**), I can move on to the search feature.  If there weren't any articles found in the timeframe (`time_frameFilterPassed` is **false**), I don't bother searching and just display a message on the screen saying no articles were found.

```Python
# If the previous test failed, don't search for anything
if time_frameFilterPassed:
    # Only retrieve the summary if we passed the time test
    summary = article.find("p", class_="summary").get_text()
    # If searchFilter is off, filter passed, otherwise, check the users search and pass the filter accordingly.
    if searchFilterON:
        if re.search(search, summary, re.IGNORECASE) is not None:
            searchFilterPassed = True
        else:
            searchFilterPassed = False
    else:
        searchFilterPassed = True
else:
    searchFilterPassed = False
```

If both filters pass, then I gather the information I want to display to the page for each article pass the list of articles to the template page.

<br>

*Table of Contents*
* **[CRUD Pages](#crud-pages)**
* **[AmiiboAPI](#amiibo-api)**
* **[Web Scraping](#web-scraping)**