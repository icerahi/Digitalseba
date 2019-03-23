from django.shortcuts import render
from django.http import HttpResponse
from .models import Gift
from home.models import Order
# Create your views here.

def gift(request):
    product=Gift.objects.all().order_by('-date')

    context={'title':'Gift',
    'product':product.filter(active=True),
    }
    return render(request,'gift.html',context)

def gift_single(request,pk):
    product=Gift.objects.get(pk=pk)
    similar=Gift.objects.order_by('?')[:4]

    context={
    'product':product,'similar':similar,
    }
    return render(request,'single.html',context)
def gift_order(request,pk):
    product=Gift.objects.get(pk=pk)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')

        city=request.POST.get('city')
        quantity=request.POST.get('quantity')
        p_name=request.POST.get('product_name')
        p_code=request.POST.get('product_code')
        price=request.POST.get('price')

        order=Order(product_name=p_name,product_code=p_code,
        price=price,quantity=quantity,customar_name=name,customar_mail=email,
        customar_phone=phone, address=address,customar_city=city).save()



    context={
    'product':product,

    }

    return render(request,'order.html',context)
