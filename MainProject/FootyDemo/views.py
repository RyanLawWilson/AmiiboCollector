import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jersey
from .forms import JerseyForm
from .api_service import *
from django.utils import timezone

# Create your views here.


def index(request):
    get_jerseys = Jersey.Jerseys.all()
    context = {'jerseys': get_jerseys}
    return render(request, 'FootyDemo/footy_index.html', context)


def add_jersey(request):
    form = JerseyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('footy')
    else:
        print(form.errors)
        form = JerseyForm()
    return render(request, 'FootyDemo/footy_create.html', {'form':form})


def details_jersey(request, pk):
    pk = int(pk)
    jersey = get_object_or_404(Jersey, pk=pk)
    context={'jersey':jersey}
    return render(request,'FootyDemo/footy_details.html', context)


def edit_jersey(request, pk):
    pk = int(pk)
    jersey = Jersey.Jerseys.get(pk=pk)
    form = JerseyForm(data=request.POST or None, instance=jersey)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('jerseyDetails',pk)
        else:
            print(form.errors)
    else:
        return render(request,'FootyDemo/footy_edit.html', {'form':form})


def delete_jersey(request, pk):
    pk = int(pk)
    jersey = Jersey.Jerseys.get(pk=pk)
    context = {'jersey': jersey}
    if request.method == 'POST':
        jersey.delete()
        return redirect('footy')
    else:
        return render(request, 'FootyDemo/footy_delete.html', context)


def api_response(request):
    context = {'world': get_areas()}
    if request.method == 'POST':
        print(request.POST)
        if 'league' in request.POST:
            league_id = request.POST['league']
            matches_page = '../{}/Matches'.format(league_id)
            return redirect(matches_page)
        if 'childArea' in request.POST:
            if request.POST['submit'] == 'noFilter':
                child = request.POST['parentArea']
            else:
                child = request.POST['childArea']
            leagues = get_leagues(child)
            context.update({'leagues': leagues, 'childArea':request.POST['childArea']})

        parent = request.POST['parentArea']
        add_parents = {'parents': get_children(parent)}
        context.update(add_parents)

    return render(request, 'FootyDemo/footy_api.html', context)


def matches(request, code):
    league_dictionary= get_matches(code)
    context={'matches': []}
    for match in league_dictionary['matches']:
        local_date = convert_to_localtime(match['utcDate'])
        game= {'date': local_date,
               'winner': match['score']['winner'],
               'score_home': match['score']['fullTime']['homeTeam'],
               'score_away': match['score']['fullTime']['awayTeam'],
               'home_team': match['homeTeam']['name'],
               'away_team': match['awayTeam']['name']}
        print(game)
        context['matches'].append(game)
    context.update({'local_tz':timezone.get_current_timezone_name()})

    return render(request, 'FootyDemo/footy_matches.html', context)


def convert_to_localtime(utctime):
    localdatetime = datetime.datetime.strptime(utctime, '%Y-%m-%dT%H:%M:%SZ')
    return localdatetime
