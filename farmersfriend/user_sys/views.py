from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    context = {}
    return render(request, "user_sys/index.html", context)


def scientific_labs(request):
    context = {}
    return render(request, "user_sys/scientific_labs.html", context)


def market(request):
    context = {}
    return render(request, "user_sys/market.html", context)


def weather_forecast(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2ebe62ad7ad9ab7bf60a9e5bf054180e'
    # city = 'Ahmedabad'
    # r=requests.get(url.format(city))
    # print(r.text)
    context = {}
    return render(request, "user_sys/weather_forecast.html", context)


def farm_ed(request):
    context = {}
    return render(request, "user_sys/farm_ed.html", context)


def video_gallery(request):
    context = {}
    return render(request, "user_sys/video_gallery.html", context)


def login(request):
    context = {}
    return render(request, "user_sys/login.html", context)


def register(request):
    context = {}
    return render(request, "user_sys/register.html", context)
