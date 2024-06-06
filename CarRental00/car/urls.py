from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
path('', views.home, name='home'),
path('login/',views.login,name='login'),
path('signup/',views.signup,name='signup'),
path('join/',views.join,name='join'),

]