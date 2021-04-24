from datetime import *

from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.urls import reverse


# User = get_user_model()


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    telephone = models.CharField(max_length=12)
    user_type = models.IntegerField(default=2)
    dob = models.DateTimeField(default=date.today())
    join_date = models.DateTimeField(default=date.today())
    is_adult = models.BooleanField(default=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    book_description = models.CharField(max_length=200, null=True, blank=True)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    book_category = models.CharField(max_length=200, null=True, blank=True)
    uploaded_date = models.DateTimeField(default=date.today())

    book_img = models.ImageField(upload_to='storeapp/bookImg/', null=True, blank=True)

    def __str__(self):
        return self.book_name

    def delete(self, *args, **kwargs):
        # self.cover.delete()
        super().delete(*args, **kwargs)
