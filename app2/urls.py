# weather/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather'),  # Define URL for weather view
]
