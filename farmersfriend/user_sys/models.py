from django.db import models

# Create your models here.
class Weather(models.Model):
    cityName = models.CharField(max_length=25)

    def __str__(self):
        return self.cityName

class QueryForm(models.Model):
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=30)
    des = models.TextField()