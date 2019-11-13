from django.shortcuts import render, redirect, get_object_or_404
from .models import Jersey
from .forms import JerseyForm
from .api_service import *

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
    context = GetAreas()
    print(context)
    return render(request, 'FootyDemo/footy_api.html', context)