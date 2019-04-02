from django.db import models


class ImportedProduct(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    id_product = models.BigIntegerField()
    nutrition_grade = models.CharField(max_length=1)
    description = models.TextField()
    picture = models.ImageField(upload_to="pics/")

