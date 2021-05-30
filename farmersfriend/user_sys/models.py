from django.db import models

# Create your models here.
class Weather(models.Model):
    cityName = models.CharField(max_length=25)

    def __str__(self):
        return self.cityName

class QueryForm(models.Model):
    phone = models.CharField(max_length=5)
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=30)
    des = models.TextField()

    def __str__(self):
        return self.query

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        form_empty = True
        for field_value in cleaned_data.itervalues():
            # Check for None or '', so IntegerFields with 0 or similar things don't seem empty.
            if field_value is not None and field_value != '':
                form_empty = False
                break
        if form_empty:
            raise forms.ValidationError(ugettext_lazy("You must fill at least one field!"))
        return cleaned_data   # Important that clean should return cleaned_data!