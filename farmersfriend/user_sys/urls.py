from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('market/', views.market, name='market'),
    path('farm_ed/', views.farm_ed, name='farm_ed'),
    path('scientific_labs/', views.scientific_labs, name='scientific_labs'),
    path('weather-forecast/', views.weather_forecast, name='weather_forecast'),
    path('video-gallery/', views.video_gallery, name='video_gallery'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('newtech/', views.newtech, name='newtech'),
    path('irrigation/', views.irrigation, name='irrigation'),
    path('queryform/', views.queryform, name='queryform'),
    path('videobar/', views.videobar, name='videobar'),
    path('product/', views.product, name='product'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    
    

]
