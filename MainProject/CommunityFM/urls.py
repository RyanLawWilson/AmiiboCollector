from django.urls import path
from . import views


urlpatterns = [
    path('', views.radioHome, name='radioHome'),
    ]