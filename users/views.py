from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse

from .forms import ConnexionForm, SignUpForm


def connexion(request):
    """
    This function allows the user (previously registered) to identify himself.
    Then he can access to his favorites, delete them, save new searches, etc.
    """
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
    """
    This function allows the user to disconnect his account. He can continue
    using the website, but as a complete visitor.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect('main:home')


def signup(request):
    """
    This function creates an account for a visitor. Fields required to do so
    are a user name and a password.
    """
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

@decorator(login_required)
def account(request):
    """
    This function allows the user to access his own account, where he can
    find and manage his favorites.
    """
    user = request.user
    return render(request, 'users/account.html', {'user': user})

