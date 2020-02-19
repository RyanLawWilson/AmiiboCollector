from django.forms import ModelForm
from .models import ShelfItem


# Create the form class.
class ShelfForm(ModelForm):
    class Meta:
        model = ShelfItem
        fields = '__all__'

