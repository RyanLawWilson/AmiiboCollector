from django.forms import ModelForm
from .models import Jersey

#Create the form class.
class JerseyForm(ModelForm):
    class Meta:
        model = Jersey
        fields = '__all__'