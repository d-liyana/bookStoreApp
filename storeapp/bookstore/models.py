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
    profile_img = models.TextField(null=True, blank=True)
    img_url = models.TextField(default="https://firebasestorage.googleapis.com/v0/b/storebook-bfaf5.appspot.com/o/images%2FprofilePic_2.jpg?alt=media&token=ac63696a-68fa-4e82-8d5a-eb57084f5a6a", null=True, blank=True)

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
    cover_img = models.TextField(null=True, blank=True)
    #book_img = models.ImageField(upload_to='storeapp/bookImg/', null=True, blank=True)
    book_img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.book_name

    def delete(self, *args, **kwargs):
        # self.cover.delete()
        super().delete(*args, **kwargs)
