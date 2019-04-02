from django.db import models

import users


class SavedFavorites(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    id_product = models.BigIntegerField()
    nutrition_grade = models.CharField(max_length=1)
    description = models.TextField()
    picture = models.ImageField(upload_to="pics/")
    user_s_favorite = models.OneToOneField(users.Users,
        on_delete=models.CASCADE, related_name='favorite of a user',)
