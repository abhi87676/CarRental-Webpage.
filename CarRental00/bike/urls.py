from django.contrib import admin
from django.urls import path
from bike import views

urlpatterns = [
path('', views.home, name='home')

]