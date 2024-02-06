from django.shortcuts import render
from shop.models import Category
from shop.models import Products
# Create your views here.
def allcategories(request):
    c = Category.objects.all()
    return render(request, 'category.html', {'c': c})


def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Products.objects.filter(category=c)
    return render(request,'products.html',{'c':c , 'p':p})

def productdetails(request,p):
    p= Products.objects.get(name=p)
    return render(request, 'productdetails.html', {'p': p})




from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username = u , password = p)
        if user:
            login(request,user)
            return redirect('shop:category')
        else:
            return HttpResponse("Invalid")

    return render(request, "login.html")
def user_logout(request):
    logout(request)
    return redirect('shop:login')

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fn = request.POST['fn']
        ln = request.POST['ln']
        e = request.POST['e']

        if (p == cp):
            user = User.objects.create_user(username=u, password=p, first_name=fn, last_name=ln, email=e )
            user.save()
            return redirect('shop:category')
        else:
            return HttpResponse("Passwords are not same")
    return render(request, "register.html")
