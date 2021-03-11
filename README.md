<p align="center">
  <img src="./readme_resources/jigglypuff.png" width="100" />
  <img src="./readme_resources/title_text.png" />
  <img src="./readme_resources/king_dedede.png" width="100" />
</p>

For this project, I created a Django application. This app is themed around Amiibos.  You can create, edit, and delete your Amiibos and search for more Amiibos.  I use the [AmiiboApi](https://www.amiiboapi.com/) to search for all available Amiibos and display them on the page.  You can also look at general Nintendo news.  This page web scrapes [nintendonews.com](https://nintendonews.com/) for the latest Nintendo articles.

The database that I am using to store the Amiibos is a local database using **SQLite**.  To contact the API, I am using Python's **requests** module.  For web scraping, I am using **Beautiful Soup**.

<br>

*Table of Contents*
* **[CRUD Pages](#crud-pages)**
* **AmiiboAPI**
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


# <p align="center" name="crud-pages">AmiiboAPI</p>
An Amiibo that I used to complement my App was the [AmiiboAPI](asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf).  This API has nearly all of the Amiibos in existence as well as images to accompany them.  I use Python's `requests` module to contact the API and get data about Amiibos.

<p align="center">
    <img src="./readme_resources/API.gif" width="75%">
</p>