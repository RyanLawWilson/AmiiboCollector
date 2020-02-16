from django.urls import path
from . import views

urlpatterns = [
    path('', views.WaveHome, name='waves'),
    path('Collection/', views.index, name='listSurfType'),  # index of jerseys
    path('AddTo/', views.add_surfInfo, name='addSurfInfo'),  # index of jerseys
    #path('ApiService/', views.api_response, name='wavesApi'),  # main page for API service with dropdowns
]
