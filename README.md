# **<p align="center">Amiibo Collector</p>**
For this project, I created a Django application. This app is themed around Amiibos.  You can create, edit, and delete your Amiibos and search for more Amiibos.  I use the [AmiiboApi](https://www.amiiboapi.com/) to search for all available Amiibos and display them on the page.  You can also look at general Nintendo news.  This page web scrapes [nintendonews.com](https://nintendonews.com/) for the latest Nintendo articles.

The database that I am using to store the Amiibos is a local database using **SQLite**.  To contact the API, I am using Python's **requests** module.  For web scraping, I am using **Beautiful Soup**.

* **[CRUD Pages](#Crud-Pages)**
    * [Index](#Index)
    * Create
    * Edit
    * Details
    * Delete
* **AmiiboApi**
* **Web Scraping (Beautiful Soup)**

<br />

# <p align="center">Crud Pages</p>
**<p align="center" name="Index">Index Page</p>**
The Index page displays all of the Amiibos stored in the database.  The Amiibo information is organized in a table.  From the table you can also view more details about an Amiibo by clicking the details button on the left.

The View is pretty straight-forward: Get all of the Amiibos saved in the database with `AmiiboFigure.AmiiboFigurines.all()` and send it to the template.  `AmiiboFigure` is the model representing an Amiibo and `AmiiboFigurines` is that model's model manager.

`View`
```python
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

```

<p align="center">
    <img src="./readme_resources/Index.gif" width="75%">
</p>