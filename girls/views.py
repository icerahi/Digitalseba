from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from home.models import Order
from .models import Girls


# Create your views here.

def girls(request):
    product=Girls.objects.all().order_by('-date')
    context={"title":"girls",
    'product':product,}
    return render(request,'girls.html',context)

def girls_single(request,pk):
    product=Girls.objects.get(pk=pk)
    similar=Girls.objects.order_by('?')[:4]
    context={
    'product':product,'similar':similar,
    }
    return render(request,'single.html',context)

def girls_order(request,pk):
    product=Girls.objects.get(pk=pk)

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
        messages.success(request, 'Thanks for your Order! Sir. We will contact you very soon!')
        return redirect('home')

    context={
    'product':product
    }

    return render(request,'order.html',context)
