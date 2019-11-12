from django.db import models

# Create your models here.
JERSEY_MANUFACTURERS = (('Adidas', 'Adidas'), ('Nike', 'Nike'), ('Puma', 'Puma'), ('Umbro', 'Umbro'), ('New Balance', 'New Balance'), ('Hummel', 'Hummel'),
                        ('Under Armour', 'Under Armour'), ('Kappa', 'Kappa'), ('Macron', 'Macron'), ('Joma', 'Joma'), ('Other', 'Other'))

class Jersey(models.Model):
    team = models.CharField(max_length=30)
    country = models.CharField(max_length=20, blank=True)
    manufacturer = models.CharField(max_length=20, choices= JERSEY_MANUFACTURERS)
    size = models.CharField(max_length=20)
    primary_color = models.CharField(max_length=20, blank=True)
    authentic = models.BooleanField(blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)

    Jerseys = models.Manager()

    def __str__(self):
        return self.team
