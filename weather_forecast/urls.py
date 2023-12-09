from django.urls import path
from .views import TemperatureForecast 

urlpatterns = [
    path('temperatures/', TemperatureForecast.as_view()),
]