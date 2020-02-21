from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.bookBagHome, name='bookBagHome'),                                       # HOME PAGE
    path('AddToLibrary/', views.add_book, name='createBook'),                              # ADD BOOK TO LIBRARY
    path('Library/', views.index, name='listBooks'),                                       # VIEW LIBRARY
    path('Library/<int:pk>/Details/', views.details_book, name='bookDetails'),             # VIEW SINGLE BOOK DETAIL
    path('Library/<int:pk>/Edit/', views.edit_book, name='bookEdit'),                      # EDIT SINGLE BOOK DETAIL
    path('Library/<int:pk>/Delete/', views.delete_book, name='bookDelete'),                # DELETE A BOOK
    path('Confirm/', views.confirmDelete_book, name='bookConfirm'),
    ]