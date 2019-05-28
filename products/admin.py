from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   model = Product
   verbose_name = 'Produits disponibles'
