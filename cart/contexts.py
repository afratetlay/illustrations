from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0  
    cart = request.session.get('cart', {})

    for item_id,  in cart.items ():
        product = get_object_or_404(Product, pk=item_id)
        total = product.price
        cart_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }
    return context