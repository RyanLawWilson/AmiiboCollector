from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.wolves_home, name='wolves_home'),
    path('create', views.wolves_create, name='createPlayer'),
    path('view', views.wolves_players, name='viewPlayers'),
    path('view/<int:pk>/Details/', views.details_player, name='playerDetails'),
    path('view/<int:pk>/Edit/', views.edit_player, name='editPlayer'),
    path('view/<int:pk>/Delete/', views.delete_player, name='deletePlayer'),
]
