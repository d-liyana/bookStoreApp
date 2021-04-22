import itertools
from datetime import *

import pyrebase
from django.contrib import auth, messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from firebase_admin import storage

from . import models
from .forms import BookForm, UserForm
from .models import User, Book

config = {
    "apiKey": "AIzaSyD1zDWPq2eQTFkka411bTJ70713VGSv6DY",
    "authDomain": "storebook-bfaf5.firebaseapp.com",
    "projectId": "storebook-bfaf5",
    "storageBucket": "storebook-bfaf5.appspot.com",
    "messagingSenderId": "41246072940",
    "appId": "1:41246072940:web:53c94572ac6d9a9ff43849",
    "measurementId": "G-EJXBPKLTL3",
    "databaseURL": ""

}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


# Shared Views

def home(request):
    return render(request, 'home/home.html', {})


def login(request):
    return render(request, 'registration/login.html', {})


def userView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            print(user.user_type)
            if user.user_type == 0 or user.is_superuser:
                return redirect('admins')
            elif user.user_type == 1:
                return redirect('customer')
            else:
                return redirect('customerChild')

        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')


def admins(request):
    book = Book.objects.all().count()
    user = User.objects.all().count()
    context = {'book': book, 'user': user}
    return render(request, 'admin/home.html')


def logoutView(request):
    logout(request)
    return redirect('home')


def register(request):
    return render(request, 'registration/register.html')


def registerView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)
        dob = request.POST['dob']
        today = timezone.now().year
        y, m, d = request.POST['dob'].split('-')

        print(dob)
        print(y)

        if today - int(y) > 18:
            is_adult = True
            user_type = 1
        else:
            is_adult = False
            user_type = 2

        if username is exit:
            messages('Username already exits')
        else:
            a = User(first_name=first_name, last_name=last_name, username=username, email=email,
                     password=password, user_type=user_type, is_active=True, dob=dob,
                     is_adult=is_adult)
        a.save()

        messages.success(request, 'Account has created successfully')
        return redirect('login')
    else:
        messages.error(request, 'Registration fail, try again later')
        return redirect('register')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class BuyBook(LoginRequiredMixin, CreateView):
    model = Book


#  template_name = 'home/buyBook.html'
#  success_url = reverse_lazy('manageBook')
#  success_message = 'You have ordered the book'


# ADMIN
@login_required
def aSearch(request):
    query = request.GET['query']
    print(type(query))
    print(query)

    data = query.split()
    data = query
    print(len(data))
    if (len(data) == 0):
        return redirect('home')
    else:
        a = data

        # Searching for It
        qs5 = models.Book.objects.filter(book_name__iexact=a).distinct()
        qs6 = models.Book.objects.filter(book_name__exact=a).distinct()
        qs7 = models.Book.objects.all().filter(book_name__contains=a)
        qs8 = models.Book.objects.select_related().filter(book_name__contains=a).distinct()
        qs9 = models.Book.objects.filter(book_name__startswith=a).distinct()
        qs10 = models.Book.objects.filter(book_name__endswith=a).distinct()
        qs11 = models.Book.objects.filter(book_name__istartswith=a).distinct()
        qs12 = models.Book.objects.all().filter(book_name__icontains=a)
        qs13 = models.Book.objects.filter(book_name__iendswith=a).distinct()

        files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

        res = []
        for i in files:
            if i not in res:
                res.append(i)

        # word variable will be shown in html when user click on search button
        word = "Searched Result :"
        print("Result")

        print(res)
        files = res

        page = request.GET.get('page', 1)
        paginator = Paginator(files, 10)
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)

        if files:
            return render(request, 'admin/searchResult.html', {'files': files, 'word': word})
        return render(request, 'admin/searchResult.html', {'files': files, 'word': word})


@login_required
def addBook(request):
    return render(request, 'admin/addBook.html', {})


@login_required
def add_book(request):
    if request.method == 'POST':
        current_user = request.user
        username = current_user.username

        book_name = request.POST['book_name']
        author = request.POST['author']
        published_year = request.POST['published_year']
        publisher = request.POST['publisher']
        book_description = request.POST['book_description']
        book_category = request.POST['book_category']
        uploaded_by = username
        user_id = current_user.id
        book_img = request.FILES['book_img']
        print(book_img)
        print(book_category)
        storage_file_path = "images/" + str(book_name) + "_" + str(book_img)
        storage.child(storage_file_path).put(book_img)

        a = Book(book_name=book_name, author=author, published_year=published_year, publisher=publisher,
                 book_description=book_description, uploaded_by=uploaded_by, user_id=user_id,
                 book_category=book_category)
        a.save()
        messages.success(request, 'Book has uploaded successfully')
        return redirect('newBook')
    else:
        messages.error(request, 'Book has not uploaded successfully')
        return redirect('addBook')


class BookList(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'admin/viewBookList.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.order_by('-id')


class ManageBook(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'admin/manageBook.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.order_by('-id')


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'admin/deleteBook.html'
    success_url = reverse_lazy('manageBook')
    success_message = 'Book has deleted successfully'


class ViewBook(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'admin/bookDetails.html'


class EditView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'admin/editBook.html'
    success_url = reverse_lazy('manageBook')
    success_message = 'Data has updated successfully'


class ViewUserList(generic.ListView):
    model = User
    template_name = 'admin/viewUserList.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')


class ViewUser(DetailView):
    model = User
    template_name = 'admin/userDetails.html'


class EditUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'admin/editUser.html'
    success_url = reverse_lazy('allUsers')
    success_message = "Data successfully updated"


class DeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'admin/deleteUser.html'
    success_url = reverse_lazy('allUsers')
    success_message = "Data successfully deleted"


def createNewUser(request):
    return render(request, 'admin/addUser.html')


def createUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        telephone = request.POST['telephone']
        user_type = request.POST['user_type']
        password = request.POST['password']
        password = make_password(password)
        dob = request.POST['dob']
        today = timezone.now().year
        y, m, d = request.POST['dob'].split('-')

        if today - int(y) > 18:
            is_adult = True
        else:
            is_adult = False
        if username is exit:
            messages('Username already exits')
        else:
            a = User(first_name=first_name, last_name=last_name, username=username, email=email,
                     password=password, user_type=user_type, telephone=telephone, is_active=True, dob=dob,
                     is_adult=is_adult)
        a.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('allUsers')

    else:
        messages.success(request, 'User has not created')
        return redirect('createNewUser')


# Common to Customers

def profile(request):
    book = Book.objects.all().count()
    user = User.objects.all().count()
    context = {'book': book, 'user': user}
    return render(request, 'customer/profile.html')


class ViewCusBook(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'customer/bookDetails.html'


# ADULT CUSTOMER

def customer(request):
    book = Book.objects.all().count()
    user = User.objects.all().count()
    context = {'book': book, 'user': user}
    return render(request, 'customer/manageCusBook.html', context)


class ManageCusBook(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'customer/manageCusBook.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.order_by('-id')


@login_required
def cusSearch(request):
    query = request.GET['query']
    print(type(query))

    # data = query.split()
    data = query
    print(len(data))
    if (len(data) == 0):
        return redirect('customer')
    else:
        a = data

        # Searching for It
        qs5 = models.Book.objects.filter(id__iexact=a).distinct()
        qs6 = models.Book.objects.filter(id__exact=a).distinct()
        qs7 = models.Book.objects.all().filter(id__contains=a)
        qs8 = models.Book.objects.select_related().filter(id__contains=a).distinct()
        qs9 = models.Book.objects.filter(id__startswith=a).distinct()
        qs10 = models.Book.objects.filter(id__endswith=a).distinct()
        qs11 = models.Book.objects.filter(id__istartswith=a).distinct()
        qs12 = models.Book.objects.all().filter(id__icontains=a)
        qs13 = models.Book.objects.filter(id__iendswith=a).distinct()

        files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

        res = []
        for i in files:
            if i not in res:
                res.append(i)

        # word variable will be shown in html when user click on search button
        word = "Searched Result :"
        print("Result")

        print(res)
        files = res

        page = request.GET.get('page', 1)
        paginator = Paginator(files, 10)
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)

        if files:
            return render(request, 'customer/result.html', {'files': files, 'word': word})
        return render(request, 'customer/result.html', {'files': files, 'word': word})


# CHILD CUSTOMER


def customerChild(request):
    user = User.objects.all().count()
    childBooks = Book.objects.filter(book_category=1)
    context = {'childBooks': childBooks, 'user': user}
    print(childBooks)
    print(Book.book_category)

    print(context)
    return render(request, 'customer/manageChildCusBook.html', context)


class ManageChildCusBook(LoginRequiredMixin, ListView):
    model = Book
    if model.book_category == '1':
        template_name = 'customer/manageChildCusBook.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.order_by('-id')
