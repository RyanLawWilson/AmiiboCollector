from django.shortcuts import render
from.models import Player
from.forms import PlayerForm
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def wolves_home(request):
    return render(request, "TWolvesRoster/wolves_home.html")


def wolves_create(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('viewPlayers')
    else:
        print(form.errors)
        form = PlayerForm()
    return render(request, "TWolvesRoster/wolves_create.html", {'form':form})


def wolves_players(request):
    return render(request, "TWolvesRoster/wolves_players.html")
