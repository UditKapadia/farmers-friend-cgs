from django.contrib import admin

# Register your models here.

# i am doing this
from .models import *

admin.site.register(Weather)
admin.site.register(QueryForm)
admin.site.register(LaboratoryBooking)
