from django.urls import path
from . import views

urlpatterns = [
    path('api/genres', views.genres, name='genres'),
    path('api/actors', views.actors, name='actors'),
    path('api/directors', views.directors, name='directors'),
]
