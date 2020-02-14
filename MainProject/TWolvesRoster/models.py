from django.db import models

# Create your models here.

POSITION_OPTIONS = (('Point Guard', 'Point Guard'), ('Shooting Guard', 'Shooting Guard'), ('Small Forward', 'Small Forward'),
                    ('Power Forward', 'Power Forward'), ('Center', 'Center'))

STATUS_OPTIONS = (('Current Player', 'Current Player'), ('Retired', 'Retired'), ('Plays for another team', 'Plays for another team'))


class Player(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    position = models.CharField(max_length=75, choices=POSITION_OPTIONS)
    currentStatus = models.CharField(max_length=75, choices=STATUS_OPTIONS)
    age = models.PositiveIntegerField(blank=True, null=True)

    Players = models.Manager()

    def __str__(self):
        return self.name
