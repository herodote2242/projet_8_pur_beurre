from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    """
    This special class is used to feed the database with products from the
    OpenFoodFact's API.
    """

    def handle(self, *args, **kargs):
        # faire une fonction pour récupérer les produits depuis OFF
        # dl quelques catégories 20 cat, 250 produits chacun,
        # le reste pour les users et leurs favoris

        # récupérer chaque produit en base
        # product.object.create 
        # récupérer sur le p5 le database_feeder. utiliser la logique de nettoyage
        # récupérer les nouvelles infos (images, urls)

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
