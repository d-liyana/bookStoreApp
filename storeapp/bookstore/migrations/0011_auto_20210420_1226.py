# Generated by Django 3.2 on 2021-04-20 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0010_auto_20210420_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_adult',
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 12, 26, 27, 179343), verbose_name='dob'),
        ),
    ]
