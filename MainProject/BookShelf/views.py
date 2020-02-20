from django.shortcuts import render, redirect
from .forms import ShelfForm
from .models import ShelfItem

# Create your views here.


def home(request):
    return render(request, 'BookShelf/bookshelf_home.html')


def index(request):
    get_books = ShelfItem.ShelfItems.all()       # get all books from the database
    content = {'books': get_books}               # creates a dictionary object of all the books for the template
    return render(request, 'BookShelf/bookshelf_index.html', content)


def add_book(request):
    form = ShelfForm(request.POST or None)      # gets the posted form
    if form.is_valid():                         # checks the form for errors and make sure its filled in
        form.save()                             # saves the valid form to the database
        return redirect('bookshelf')            # redirects to the index page
    else:
        print(form.errors)                      # prints any errors to the terminal
        form = ShelfForm()                      # creates a new blank form
    return render(request, 'BookShelf/bookshelf_create.html', {'form': form})



