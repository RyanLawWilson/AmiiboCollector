from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.bookBagHome, name='bookBagHome'),                                #home page
    ]