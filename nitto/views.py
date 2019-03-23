from django.shortcuts import render
from django.http import HttpResponse
from .models import Nitto
# Create your views here.

def nitto(request):
    product=Nitto.objects.all().order_by('-date')
    context={"title":"nitto",
    'product':product,}
    return render(request,'nitto.html',context)

def nitto_single(request,pk):
    product=Nitto.objects.get(pk=pk)
    similar=Nitto.objects.order_by('?')[:4]
    context={
    'product':product,'similar':similar,
    }
    return render(request,'single.html',context)

def nitto_order(request,pk):
    product=Nitto.objects.get(pk=pk)

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
    'product':product
    }

    return render(request,'order.html',context)
