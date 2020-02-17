from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.bookBagHome, name='bookBagHome'),                #home page
    path('AddToLibrary/', views.add_book, name='createBook'),
    path('Library/', views.index, name='listBooks'),

    ]