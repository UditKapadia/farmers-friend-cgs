from django.forms import ModelForm, TextInput
from .models import * 

class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['cityName']