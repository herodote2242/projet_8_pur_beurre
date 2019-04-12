from django.db import models

from users.models import User
from products.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
        related_name='favorites_as_product')
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE,
        related_name='favorites_as_substitute')
