from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    id_product = models.BigIntegerField()
    nutrition_grade = models.CharField(max_length=1)
    description = models.TextField()
    picture_product = models.URLField()
    picture_data = models.URLField()
    category = models.ForeignKey('Category')


class Category(models.Model):
    category_name = models.CharField(max_length=75)
