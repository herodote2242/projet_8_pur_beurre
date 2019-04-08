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

