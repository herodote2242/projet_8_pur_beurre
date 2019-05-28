from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse

from .forms import ConnexionForm, SignUpForm


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
    return redirect('main:home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

