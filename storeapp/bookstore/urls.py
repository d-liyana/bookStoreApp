from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Common URL's
    path('', views.home, name='home'),
    path("login/", views.login, name="login"),
    path('userView/', views.userView, name='userView'),
    path("register/", views.register, name="register"),
    path("registerView/", views.registerView, name="registerView"),
    path('logout/', views.logoutView, name='logout'),
    path('buyBook/<int:pk>', views.BuyBook.as_view(), name='buyBook'),

    # Admin URL'
    path('admins/', views.admins, name='admins'),
    path('aSearch/', views.aSearch, name='aSearch'),
    path('addBook/', views.addBook, name='addBook'),
    path('add_book/', views.add_book, name='add_book'),
    path('newBook/', views.BookList.as_view(), name='newBook'),
    path('manageBook/', views.ManageBook.as_view(), name='manageBook'),
    path('viewBook/<int:pk>', views.ViewBook.as_view(), name='viewBook'),
    path('editBook/<int:pk>', views.EditView.as_view(), name='editBook'),
    path('deleteBook/<int:pk>', views.DeleteBook.as_view(), name='deleteBook'),
    path('createNewUser/', views.createNewUser, name='createNewUser'),
    path('allUsers/', views.ViewUserList.as_view(), name='allUsers'),
    path('createUser/', views.createUser, name='createUser'),
    path('viewUser/<int:pk>', views.ViewUser.as_view(), name='viewUser'),
    path('editUser/<int:pk>', views.EditUser.as_view(), name='editUser'),
    path('deleteUser/<int:pk>', views.DeleteUser.as_view(), name='deleteUser'),

    # Common To Customers

    path('profile/', views.profile, name='profile'),
    path('viewCusBook/<int:pk>', views.ViewCusBook.as_view(), name='viewCusBook'),
    path('editCusUser/<int:pk>', views.EditCusUser.as_view(), name='editCusUser'),

    # Adult Customer URL's

   # path('customer/', views.customer, name='customer'),
    path('customer/', views.ManageCusBook.as_view(), name='customer'),
    path('editBook/<int:pk>', views.EditView.as_view(), name='editBook'),
    path('deleteBook/<int:pk>', views.DeleteBook.as_view(), name='deleteBook'),

    # Child Customer URL's
    path('customerChild/', views.customerChild, name='customerChild'),
    path('manageChildCusBook/', views.ManageChildCusBook.as_view(), name='manageChildCusBook'),

]
