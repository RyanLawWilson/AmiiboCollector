from django.shortcuts import render


# Create your views here.

def wolves_home(request):
    return render(request, "TWolvesRoster/wolves_home.html")


def wolves_create(request):
    return render(request, "TWolvesRoster/wolves_create.html")


def wolves_players(request):
    return render(request, "TWolvesRoster/wolves_players.html")
