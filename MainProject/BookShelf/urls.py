from django.urls import path
from . import views

# For URL Patterns, the first parameter is the pattern, the second is the method you're calling inside of your view,
# and third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='bookshelf'),                 # Home page
]