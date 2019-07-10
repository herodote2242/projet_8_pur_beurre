from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('connexion/', views.connexion, name="connexion"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),
    path('signup/', views.signup, name="signup"),
    path('account/', views.account, name="account"),
]
