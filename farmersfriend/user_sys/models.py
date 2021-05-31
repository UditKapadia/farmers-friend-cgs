from django.db import models

# Create your models here.


class Weather(models.Model):
    cityName = models.CharField(max_length=25)

    def __str__(self):
        return self.cityName


class QueryForm(models.Model):
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=30)
    des = models.TextField()

    def __str__(self):
        return self.query


class LaboratoryBooking(models.Model):
    mobileNumber = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    addressField = models.TextField()
    cityField = models.CharField(max_length=30)
    stateField = models.CharField(max_length=30)
    lastCropSown = models.CharField(max_length=30)
    soilType = models.CharField(max_length=30)
    cropType = models.CharField(max_length=30)
