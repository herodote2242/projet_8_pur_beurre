import json

from django.shortcuts import render

from products import Category, Product
from favorites import Favorite


def search(request):
    """
    This function is responsible of searching the products according to what
    is written by the visitor in the search box.
    """
    product_searched = request.GET.get('page')
    user = request.user
    category = Category.objects.get(name__icontains=search_products,
        alternative=False)
    product = Product.objects.filter(catgory_id=category_id)


def details(request, product_id, product_name):
    """
    This views is used to see the details of one selected product, among the
    list of products searched.
    """
    product = Product.objects.get(id=product_id)(id=product_id)
    return render(request, 'products/templates/details.html')


def save(request):
    """
    This function allows the user to save a product as a favorite.
    """
    data = {}
    if request.method == 'POST':
        user_id = request.POST.get('usser_id')
        product_id = request.POST.get('product_id')
        Favorite.objects.create(product_id=product_id, user_id=user_id)
        return HttpResponse(
            json.dumps(data), content_type='application/json',
        )