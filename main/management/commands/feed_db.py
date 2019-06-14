import requests
from django.core.management.base import BaseCommand, CommandError

from main import config
from products.models import Category, Product


class Command(BaseCommand):
    """
    This special class is used to feed the database with products from the
    OpenFoodFact's API.
    """


    def fetch_data(self):
        """This functions collects data from the Open Food Facts API
        according to the criteria."""
        self.products = {}
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
            self.products['category'] = data['products']


    def product_invalid(self, product):
        """This function checks if a product has all the informations
        required. If a product is invalid, it returns True. If it is valid
        it returns False. Only in this case we can save it in the database.
        """
        keys = ("code", "product_name", "brands", "categories_fr",
                "url_link", "nutrition_grade_fr", "description",
                "image_url", "image_small_url")
        for key in keys:
            if key not in product or not product[key]:
                return True
        return False


    def handle(self, *args, **kargs):
        """This function is called to feed the local database. If the
        'product_invalid' function returns False for a product, it is
        saved in the local database, with its keys filling the columns.
        """
        self.fetch_data()
        for category in self.products:
            category = Category.objects.get_or_create(category_name=category)
            for product in self.products['category']:
                if self.product_invalid(product):
                    continue
                product = Product.objects.create(name=product['product_name'],
                    id_product=product['code'], nutrition_grade=
                    product['nutrition_grade_fr'], category=category,
                    brand=product['brands'], url=product['url_link'], description=
                    product['description'], image_url=product['image_url'],
                    image_small_url=product['image_small_url'])

