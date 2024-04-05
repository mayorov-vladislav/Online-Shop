from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

# Create your views here.
def cart_add(request):
    product = Products.objects.get()

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META['HTTP_REFERER'])
def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...