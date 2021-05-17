from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('market/',views.market, name='market'),
    path('farm_ed/',views.farm_ed, name='farm_ed'),
    path('scientific_labs/',views.scientific_labs, name='scientific_labs'),
    path('weather-forecast/',views.weather_forecast, name='weather_forecast'),
]