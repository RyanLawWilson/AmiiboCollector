from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book


# Function that renders the home page
def bookBagHome(request):
    return render(request, 'BookBag/bookBag_home.html')


# Function to add a new book to collection
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('createBook')
    else:
        print(form.errors)
        form = BookForm()
    return render(request, 'BookBag/bookBag_create.html', {'form': form})


# Function that controls index of books
def index(request):
    get_books = Book.Books.all()
    context = {'books': get_books}
    return render(request, 'BookBag/bookBag_index.html', context)
