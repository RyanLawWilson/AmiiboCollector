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
        return redirect('listBooks')
    else:
        print(form.errors)
        form = BookForm()
    return render(request, 'BookBag/bookBag_create.html', {'form': form})


# Function that controls index of books
def index(request):
    get_books = Book.Books.all()
    context = {'books': get_books}
    return render(request, 'BookBag/bookBag_index.html', context)


# Function to get details of a single book
def details_book(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'BookBag/bookBag_details.html', context)


# Function to edit details of a single book
def edit_book(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('bookDetails', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'BookBag/bookBag_edit.html', {'form': form})


# Function to delete book in library
def delete_book(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('listBooks')
    return render(request, 'BookBag/bookBag_confirm.html', {'book': book})


# Function to confirm deletion of book
def confirmDelete_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('listBooks')
        else:
            return redirect('listBooks')
