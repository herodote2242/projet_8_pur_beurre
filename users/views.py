from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms import ConnexionForm


def connexion(request):
    if request.user.is_authenticated:
        return HttpResponse("Bienvenue, {0}. Vous êtes déjà connecté(e) !"
            .format(request.user.username))
    else:
        error = False
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                else:
                    error = True
        else:
            form = ConnexionForm()
        return render(request, 'users/login.html', locals())


def deconnexion(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main/home.html')


def signup(request):
    return render(request, 'users/signup.html')
