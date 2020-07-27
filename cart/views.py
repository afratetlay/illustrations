from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view to the cart page """

    return render(request, "cart/cart.html")

def add_to_bag(request, item_id):
    """ Add items to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        if item_id:
            bag.pop(item_id) 
        
        request.session['cart'] = cart 
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)