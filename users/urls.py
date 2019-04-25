from django.urls import path
from . import views


urlpatterns = [
    path(r'^log_in$', views.log_in, name="log in"),
    path(r'^log_out$', views.log_out, name="log out"),
    path(r'^sign_up$', views.sign_up, name="sign up"),
]
