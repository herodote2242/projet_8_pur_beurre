from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product
from products.forms import SearchForm


def home(request):
    form = SearchForm()    
    return render(request, 'main/home.html', {'form':form})


def autocomplete(request):
    term = request.GET.get('term')
    # To receive the 20 first products ordered by the nutrition grade :
    products = Product.objects.filter(name__icontains=term).order_by('-nutrition_grade')[:20]
    # To receive all the answers in a object list :
    products_list = [product.name for product in products]
    return JsonResponse(products_list, safe=False)
