from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   model = Product
   verbose_name = 'Produit Sauvegardé'
