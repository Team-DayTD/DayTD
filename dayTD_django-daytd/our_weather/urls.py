from django.urls import path
from . import views
from .views import *

app_name = 'our_weather'

urlpatterns=[
    path('', WeatherListAPI.as_view()),
    path('detail/', views.detail, name='detail'),
    path('gps/', views.gps, name='gps')
]