from django.urls import path, include
from django.contrib import admin

from . import views


app_name = 'main'
urlpatterns = [
    path('details/', views.details, name="details"),
    path('search/', views.search, name="search"),
    path('favorite/', views.favorite, name="favorite"),
]