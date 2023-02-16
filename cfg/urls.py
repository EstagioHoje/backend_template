from django.contrib import admin
from django.urls import path, include
from src.main import hello_world

urlpatterns = [
    path(r'', hello_world)
]