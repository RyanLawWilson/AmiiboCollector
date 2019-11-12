from django.shortcuts import render
from .models import Jersey
from .forms import JerseyForm

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