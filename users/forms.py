from django import forms


class ConnexionForm(forms.Form):
    """
    This class is responsible of creating the form for the connexion of the
    user.
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)
