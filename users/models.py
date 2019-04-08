from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)


# créer un propre user hérité de base_user pour créer un utilisateur juste mail + 
