# Generated by Django 3.2 on 2021-04-21 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0016_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploaded_date',
            field=models.DateTimeField(default=datetime.date(2021, 4, 21)),
        ),
    ]
