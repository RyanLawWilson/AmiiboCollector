from django.urls import path
from . import views

# For URL Patterns, the first parameter is the pattern, the second is the method you're calling inside of your view,
# and third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='bookshelf'),                         # Home page
    path('AddToShelf', views.add_book, name='addbook'),             # create a book object to database
    path('ViewShelf', views.index, name='listshelf'),               # index page listing objects in database
    path('ViewShelf/Details/<int:pk>', views.details, name='showdetail'),   # gathers data for single object and
                                                                            # displays it
]