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
* **Web Scraping**

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
An Amiibo that I used to complement my App was the [AmiiboAPI](asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf).  This API has nearly all of the Amiibos in existence as well as images to accompany them.  I use Python's `requests` module to contact the API and get data about Amiibos.

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