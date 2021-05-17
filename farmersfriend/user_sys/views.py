from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request,"user_sys/index.html", context)

def scientific_labs(request):
    context={}
    return render(request,"user_sys/scientific_lab",context)

def market(request):
    context={}
    return render(request,"user_sys/market",context)

def weather_forecast(request):
    context={}
    return render(request,"user_sys/weather_forecast",context)

def farm_ed(request):
    context={}
    return render(request,"user_sys/farm_ed",context)
