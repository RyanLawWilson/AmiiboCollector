from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookBagHome, name='bookBagHome'),                                #home page
    ]
