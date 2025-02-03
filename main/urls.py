
from django.contrib import admin
from django.urls import path
from .views import index,home

urlpatterns = [
    path('index/',index),
    path('home/', home),


]
