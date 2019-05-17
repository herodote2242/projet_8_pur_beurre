from django.db import models


class Product(models.Model):
    """
    This class represents the different kind of products that are present in
    the database. Each product has several caracteristics, such as its name,
    brand, id, nutrition grade ...
    """
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    id_product = models.BigIntegerField(primary_key=True)
    nutrition_grade = models.CharField(max_length=1)
    description = models.TextField()
    picture_product = models.URLField()
    picture_data = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
        related_name='products')


class Category(models.Model):
    """
    Each product can be stored in one and only one category, to make it simple.
    Of course in reality, it can has multiple categories, but for our project,
    it is simpler to find a good substitute when the product searched and the
    answers are in the same category. Check the readme.txt to know the few
    categories existing in this project.
    """
    category_name = models.CharField(max_length=75)


class Favorite(models.Model):
    """
    A favorite is stored in the database when a particular user finds a
    particular product.
    """
    favorite_name = models.ForeignKey('Product', on_delete=models.DO_NOTHING,
        related_name='favorite')
    registered_user = models.ForeignKey('User', on_delete=models.DO_NOTHING,
        related_name='registered user')