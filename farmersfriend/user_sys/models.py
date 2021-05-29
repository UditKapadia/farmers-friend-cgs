from django.db import models

# Create your models here.
class Weather(models.Model):
    cityName = models.CharField(max_length=25)

    def __str__(self):
        return self.cityName