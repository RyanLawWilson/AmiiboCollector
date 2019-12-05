from django.urls import include, path
from . import views

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='footy'),                                #home page
    path('Collection/', views.index, name='listJerseys'),               #index of jerseys
    path('AddToCollection/', views.add_jersey, name='createJersey'),    #add new jersey
    path('Collection/<int:pk>/Details/', views.details_jersey, name='jerseyDetails'),  #get details for a single jersey
    path('ApiService/', views.api_response, name='footyApi'),           #main page for API service with dropdowns
    path('<int:code>/Matches/', views.matches, name='footyMatches'),    #specific league page for matches
    path('MLSNews/', views.mls_news, name='MLSNews'),                   #data scraped news from MLS
    ]