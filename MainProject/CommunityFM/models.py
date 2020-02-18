from django.db import models

# Create your models here.



class Station(models.Model):
    station_name = models.CharField(max_length=30)
    station_frequency = models.DecimalField(max_digits=4, decimal_places=1)
    genre = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    station_url = models.URLField(max_length=300, default="http://")

    objects = models.Manager()

    def __str__(self):
        return self.station_name