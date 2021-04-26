from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Book
from .models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'published_year', 'publisher', 'uploaded_by', 'cover_img', 'book_description',
                  'book_category', 'uploaded_date', 'book_img')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'telephone', 'user_type', 'dob',
                  'is_active', 'join_date', 'is_adult','profile_img','img_url')
