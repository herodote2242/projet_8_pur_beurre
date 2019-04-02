from django.db import models

import favorites as favs


class Users(models.Model):
    id_user = models.AutoField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=75)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)
    favorites = models.ForeignKey(favs.SavedFavorites,
        on_delete=models.CASCADE,)
