from django.forms import ModelForm, TextInput
from .models import *
from django import forms


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['cityName']
