from django.forms import ModelForm
from .models import surfType

#Create the form class.
class BoardForm(ModelForm):
    class Meta:
        model = surfType
        fields = '__all__'