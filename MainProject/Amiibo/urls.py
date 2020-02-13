# The MainProject urls.py will send us here when amiibo/ is at the end of the URL

from django.urls import path
from . import views

# When you make a view, you need to make a URL so that you can access that view.  Do that here.
# Django will check the rest of the URL now...
urlpatterns = [
	# If the end of the URL is blank, go to views.py and execute the index method
	path('', views.amiibo_home, name='amiibo_home'),
	path('yourcollection', views.amiibo_db, name='amiiboCollection'),
	path('amiibolist', views.amiibo_api, name='amiiboAPI'),
	path('nintendonews', views.amiibo_news, name='nintendoNews'),
]