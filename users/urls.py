from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.connection_view, name="connection"),
]
