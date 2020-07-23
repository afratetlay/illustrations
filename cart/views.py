from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view to the cart page """

    return render(request, 'cart/cart.html')

def add_to_bag(request, item_id):
    """ Add items to the bag """
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)