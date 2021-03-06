# Generated by Django 3.2 on 2021-04-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0023_auto_20210425_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
