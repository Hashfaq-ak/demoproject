from django.shortcuts import render
from cart.models import Cart
from shop.models import Products
# Create your views here.
def addtocart(request,n):
    p=Products.objects.get(name=n)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
            cart.save()
    except:
        if(p.stock > 0):
            cart=Cart.objects.create(product=p,user=u,quantity=1)
            cart.save()
    return cartview(request)


def cartview(request):
    u=request.user
    cart=Cart.objects.filter(user=u)
    total=0
    for i in cart:
        total=i.quantity*i.product.price
    return render(request,'cartview.html',{'c':cart,'total':total})


def remove(request,n):
    p = Products.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if (cart.quantity > 1):
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return cartview(request)

def delete(request,n):
    p = Products.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if (cart.quantity ):
            cart.delete()
        else:
            cart.delete()
    except:
        pass

    return cartview(request)
def orderform(request):
    return render(request,'orderform.html')