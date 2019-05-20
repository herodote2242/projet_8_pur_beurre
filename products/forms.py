from django import forms


class SearchForm(forms.Form):
    """
    This class creates the form used by the visitor to search a product.
    """
    product_to_search = forms.CharField(label="Rechercher un produit", max_length=100)