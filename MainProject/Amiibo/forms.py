from django.forms import ModelForm
from .models import AmiiboFigure

# This is a model form that makes it easier to create a form to input values into AmiiboFigure
class AmiiboFigureForm(ModelForm):
	class Meta:
		# Designate the model that you want the form for
		model = AmiiboFigure

		# What fields, from the model, should be in the form.
		fields = ['name','game_series','purchase_price','purchase_date','amount']