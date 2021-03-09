# **<p align="center">Amiibo Collector</p>**
For this project, I created a Django application. This app is themed around Amiibos.  You can create, edit, and delete your Amiibos and search for more Amiibos.  I use the AmiiboApi to search for all available Amiibos and display them on the page.  You can also look at general Nintendo news.  This page web scrapes [nintendonews.com](https://nintendonews.com/) for the latest Nintendo articles.

The database that I am using to store the Amiibos is a local database using **SQLite**.  To contact the API, I am using Python's **requests** module.  For web scraping, I am using **Beautiful Soup**.

## Table of Contents

* **[CRUD Pages](#Crud-Pages)**
    * [Index](##Index)
    * Create
    * Edit
    * Details
    * Delete
* **AmiiboApi**
* **Web Scraping (Beautiful Soup)**

<br />

# <p align="center">Crud Pages</p>
## Index
The Index page displays all of the Amiibos stored in the database.

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
    <img src="./readme_resources/API.gif" width="720px">
</p>