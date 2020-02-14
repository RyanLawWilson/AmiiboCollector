# The MainProject urls.py will send us here when amiibo/ is at the end of the URL

from django.urls import path
from . import views

# When you make a view, you need to make a URL so that you can access that view.  Do that here.
# Django will check the rest of the URL now...
urlpatterns = [
	# If the end of the URL is blank, go to views.py and execute the index method
	path('', views.amiibo_home, name='amiibo_home'),

	path('your-amiibo-collection/', views.amiibo_db, name='amiiboCollection'),
	# I think what is actually happening is Django compares the URL with the name attribute.
	# If it matches, the URL is set to the first argument in path().
	path('your-amiibo-collection/addAmiibo/', views.addAmiibo, name='addAmiibo'),
	path('your-amiibo-collection/<int:pk>/amiibo_details/', views.amiibo_details, name='amiiboDetails'),

	path('amiibolist/', views.amiibo_api, name='amiiboAPI'),
	path('nintendonews/', views.amiibo_news, name='nintendoNews'),



]