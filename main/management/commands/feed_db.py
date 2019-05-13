import requests
from django.core.management.base import BaseCommand, CommandError

import config
#ci dessous à modifier
from products.models import Category, Product


class Command(BaseCommand):
    """
    This special class is used to feed the database with products from the
    OpenFoodFact's API.
    """

    def handle(self, *args, **kargs):
        # récupérer chaque produit en base
        # product.object.create 
        pass

    def fetch_data(self):
        """This functions collects data from the Open Food Facts API
        according to the criteria."""
        products = {}
        for category in config.CATEGORIES_TO_RECOVER:
            url = "https://fr.openfoodfacts.org/cgi/search.pl"
            criteria = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category,
                "sort_by": "product_name",
                "page_size": config.NUMBER_OF_PRODUCTS,
                "json": 1
            }
            req = requests.get(url, params=criteria)
            data = req.json()
            products['category'] = data['products']

    def product_invalid(self, product):
        """This function checks if a product has all the informations
        required. If no, it is invalid. If yes, it is valid and can
        be saved in the database.
        """
        keys = ("code", "product_name", "brands", "pictures",
                "categories", "url", "nutrition_grade_fr")
        for key in keys:
            if key not in product or not product[key]:
                return True
        return False
