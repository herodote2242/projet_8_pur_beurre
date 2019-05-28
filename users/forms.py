from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    """
    This class is responsible of creating the form for the connexion of the
    user.
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """
    With this class, a visitor can register his profile in the database. It
    allows the visitor to be a member, to log in and log out, and of course
    to be able to save favorites.
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
        required=False, help_text='Optionnel')
    email = forms.EmailField(label="Adresse mail", widget=forms.EmailInput,
        max_length=254, required=True, help_text=
        'Obligatoire. Renseignez une addresse mail valide.')
    password1 = forms.CharField(label="Mot de passe",
        widget=forms.PasswordInput, help_text='Obligatoire.')
    password2 = forms.CharField(
        label="Vérification du mot de passe saisi",
        widget=forms.PasswordInput, help_text='Obligatoire.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
