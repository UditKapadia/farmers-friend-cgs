# Generated by Django 3.2.2 on 2021-05-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sys', '0005_alter_laboratorybooking_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorybooking',
            name='mobileNumber',
            field=models.CharField(default='1234567890', max_length=30),
        ),
    ]
