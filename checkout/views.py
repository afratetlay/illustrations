from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HC1CLFRX4Llp0XJIYZB02UZ4upX3Sa4Y5XHDzRN7MOPdmHTV2j4cnmtnay5v3C5ME0KaUVvme6VSZaRIWYzjLBu00xSwi2Cp2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    return render(request, 'checkout.html', context)