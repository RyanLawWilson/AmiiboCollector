from django.forms import ModelForm
from .models import Station

#create the form class
class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = '__all__'