from django.urls import path, include
from . import views


urlpatterns = [
    path('connection/', include(users.connection_view)),
]
