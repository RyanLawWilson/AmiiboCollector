"""
Story #2

Create a model for the collection item you will be tracking and add the ability to create a new item.

1) Create your model and add a migration, make sure to plan out all the categories you want to track for your object. Include an objects manager for accessing the database.
	- I'll store:
		Name (NOT NULL),
		Game Series (NOT NULL),
		Purchase Price (NULL),
		Purchase Date (NULL),
		Amount (NULL)
	- DONE
2) Create a model form that will include any inputs the user needs to make
	- DONE go to forms.py
3) Add a template to your app folder for creating a new item.
	- DONE
4) Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
	- DONE
5) Check the database to make sure your item saves without errors.
	- DONE
6) Add whatever styling is appropriate to your templates.
	- Done
"""

from django.db import models

# Defining my Amiibo Table
class AmiiboFigure(models.Model):

	AMOUNT_CHOICES = [
		(1, 1), (2, 2), (3, 3),
		(4, 4), (5, 5), (6, 6),
		(7, 7), (8, 8), (9, 9),
	]

	# If you add or remove columns, make sure to do the same in forms.py

	name = models.CharField(max_length=60, null=False, blank=False)
	game_series = models.CharField(max_length=60, null=False, blank=False)
	purchase_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	purchase_date = models.CharField(max_length=60, null=True, blank=True)
	amount = models.PositiveSmallIntegerField(default=1, null=False, blank=False, choices=AMOUNT_CHOICES)

	AmiiboFigurines = models.Manager()

	def __str__(self):
		return self.name