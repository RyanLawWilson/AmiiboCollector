from django.db import models

# Create your models here.
BOOK_TYPE = (('Fiction', 'Fiction'), ('Nonfiction', 'Nonfiction'))

BOOK_RATING = (('Loved it', 'Loved it'), ('Liked it', 'Liked it'), ('Tolerated it', 'Tolerated it'),
               ('Hated it', 'Hated it'))


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=BOOK_TYPE)
    genre = models.CharField(max_length=30)
    rating = models.CharField(max_length=15, choices=BOOK_RATING)

    Books = models.Manager()