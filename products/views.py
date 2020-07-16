from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all of the products, including the sorting and the search queries """


    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)