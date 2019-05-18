from django import forms


class ConnexionForm(forms.Form):
    """
    This class is responsible of creating the form for the connexion of the
    user.
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput)


class SearchForm(forms.Form):
    """
    This class creates the form used by the visitor to search a product.
    """
    product_to_search = forms.CharField(label="Rechercher un produit", max_length=100)

class SignUpForm(forms.Form):
    """
    With this class, a visitor can register his profile in the database. It
    allows the visitor to be a member, to log in and log out, and of course
    to be able to save favorites.
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Adresse mail", widget=forms.EmailInput)    
    password = forms.CharField(label="Mot de passe",
        widget=forms.PasswordInput)
    check_password = forms.CharField(
        label="Vérification du mot de passe saisi",
        widget=forms.PasswordInput)
