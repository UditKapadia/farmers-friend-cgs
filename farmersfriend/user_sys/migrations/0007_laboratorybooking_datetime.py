# Generated by Django 3.2.2 on 2021-05-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sys', '0006_alter_laboratorybooking_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorybooking',
            name='dateTime',
            field=models.DateField(null=True),
        ),
    ]