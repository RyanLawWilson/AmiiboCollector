from django.shortcuts import render, redirect, get_object_or_404
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

def details(request, pk):
    pk = int(pk)                                # ensures the value for the primary key is in an integer form
    book = get_object_or_404(ShelfItem, pk=pk)  # gets a single object's data from the database
    content = {'book': book}                     # creates a dictionary object to pass into the book object
    return render(request, 'BookShelf/bookshelf_details.html', content)



    # pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    # jersey = get_object_or_404(Jersey, pk=pk)   #Gets single instance of the jersey from the database
    # context={'jersey':jersey}                   #Creates dictionary object to pass the jersey object
    # return render(request,'FootyDemo/footy_details.html', context)