# Generated by Django 3.2 on 2021-04-25 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0021_auto_20210424_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploaded_date',
            field=models.DateTimeField(default=datetime.date(2021, 4, 25)),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.date(2021, 4, 25)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.date(2021, 4, 25)),
        ),
    ]
