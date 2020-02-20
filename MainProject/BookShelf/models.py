from django.db import models


# Create your models here.

class ShelfItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=300)

    ShelfItems = models.Manager()

    def __str__(self):
        return self.title
