from django.db import models

# Create your models here.
BOARD_TYPES = (('Long', 'Long'),('short', 'short'),('fish', 'fish'),('egg', 'egg'))

BOARD_LENGTHS = (("6'", "6'"),("6'-6\"", "6'-6\""),("7'", "7'"),("7'-6\"", "7'-6\""),("8'", "8'"),("8'-6\"", "8'-6\""),
               ("9'", "9'"),("9'-6\"", "9'-6\""),("10'", "10'"),("10'-6\"", "10'-6\""),("11'", "11'"),("SUP", "SUP"))

class surfType(models.Model):
    locale = models.CharField(max_length=40)
    country = models.CharField(max_length=30, blank=True)
    board_type = models.CharField(max_length=20, choices=BOARD_TYPES)
    board_length = models.CharField(max_length=20, choices=BOARD_LENGTHS)

    surfTypes = models.Manager()

    def __str__(self):
        return self.locale
