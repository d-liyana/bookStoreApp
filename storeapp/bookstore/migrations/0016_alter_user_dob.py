# Generated by Django 3.2 on 2021-04-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_auto_20210420_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(verbose_name='dob'),
        ),
    ]