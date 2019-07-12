from django.urls import path, include
from django.contrib import admin

from . import views


app_name = 'main'
urlpatterns = [
    path('save/', views.save, name="save"),
]