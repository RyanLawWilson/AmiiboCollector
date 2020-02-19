from django.urls import path
from . import views


urlpatterns = [
    path('', views.radioHome, name='radioHome'),
    path('addNewStation/', views.add_station, name='addStation'),
    path('index/', views.station_index, name='index')
    ]