from django.urls import path, include
from django.contrib import admin

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('autocomplete/', views.autocomplete, name="autocomplete"),
]
