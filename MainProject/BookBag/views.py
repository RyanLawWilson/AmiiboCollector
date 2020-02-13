from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm


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
