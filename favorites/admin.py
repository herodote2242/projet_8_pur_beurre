from django.contrib import admin

from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
   model = Favorite
   verbose_name = 'Favoris enregistrés'

