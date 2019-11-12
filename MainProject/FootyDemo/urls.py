from django.urls import include, path
from . import views

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.index, name='footy'),
    path('AddToCollection/', views.add_jersey, name='createJersey'),
    path('<int:pk>/Details/', views.details_jersey, name='jerseyDetails'),
    path('<int:pk>/Edit/', views.edit_jersey, name='jerseyEdit'),
    path('<int:pk>/Delete/', views.delete_jersey, name='jerseyDelete'),
    ]