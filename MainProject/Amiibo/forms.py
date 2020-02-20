from django.contrib.sites import requests
from django.forms import ModelForm
from .models import AmiiboFigure
from django import forms

# This is a model form that makes it easier to create a form to input values into AmiiboFigure
class AmiiboFigureForm(ModelForm):
	class Meta:
		# Designate the model that you want the form for
		model = AmiiboFigure

		# What fields, from the model, should be in the form.
		fields = ['name','game_series','purchase_price','purchase_date','amount']

# This is for the filter form in the API page.
class APIFilterForm(forms.Form):

	DATECHOICES = (
		('Before','Before'),
		('After', 'After'),
		('On','On'),
	)

	amiiboName = forms.CharField(label='Amiibo Name', max_length=60, required=False)
	characterName = forms.CharField(label='Character Name', max_length=60, required=False)
	gameSeries = forms.CharField(label='Game Series', max_length=60, required=False)
	date = forms.CharField(label='Date', max_length=60, required=False)
	dateChoices = forms.ChoiceField(label='Date Choices', choices=DATECHOICES, required=False)