from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('index/', admin.site.urls),
    path('favorites/', views.favorites_view),
    path('products/', views.products_view),
    path('database/', views.database_view),
    path('users/', views.users_view),
    path('main/', views.main_view),
]
