"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from registration.views import UserCreateView, LoginView, PasswordForgottenView, ResetPasswordView
from django.contrib.auth.views import LogoutView
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.BooksListView.as_view(), name='main'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_forgotten/', PasswordForgottenView.as_view(), name='password_forgotten'),
    re_path(r'^reset/(?P<user_id>(\d)+)/(?P<token>(\w)+)', ResetPasswordView.as_view(), name='reset_password'),
    re_path(r'^book/(?P<book_id>(\d)+)', views.BookDetailsView.as_view(), name='book_details'),
    re_path(r'^reserve/(?P<book_id>(\d)+)', views.BookReserveView.as_view(), name='reserve'),
    re_path(r'^author/(?P<author_id>(\d)+)', views.AuthorDetailsView.as_view(), name='author_details'),
    path('user/', views.UserView.as_view(), name='user'),
]
