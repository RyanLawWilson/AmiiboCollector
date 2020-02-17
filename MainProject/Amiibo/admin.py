"""
Story #1: Build the basic app (Hello World)

Create a new app for the project, named appropriately for what you are tracking,
and get it to display a home page with basic content.

1) Create new app using manage.py startapp
	- Use python manage.py startapp Amiibo
2) Register app from within MainProject > MainProject > settings.py
	- Add "Amiibo" to INSTALLED_APPS List
3) Create base and home templates in a new template folder
	- Made templates > Amiibo > amiibo_base.html and amiibo_home.html
	- *****NEED TO POPULATE THE HTML FILES*****
4) Add function to views to render the home page
	- Added
5) Register urls with MainApp and create urls.py for your app and homepage
	- Done
6) Add minimal content, such as title, image, etc, and some basic styling to home.
	- Done
"""

from django.contrib import admin
from .models import AmiiboFigure

admin.site.register(AmiiboFigure)