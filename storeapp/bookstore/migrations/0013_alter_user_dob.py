# Generated by Django 3.2 on 2021-04-20 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 12, 37, 17, 130457), verbose_name='dob'),
        ),
    ]