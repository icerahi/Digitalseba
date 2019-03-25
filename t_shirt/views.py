from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

from home.models import Order
from .models import T_shirt
# Create your views here.

def t_shirt(request):
    product=T_shirt.objects.all().order_by('-date')
    context={'title':'t_shirt',
    'product':product,}
    return render(request,'t_shirt.html',context)
def t_shirt_single(request,pk):
    product=T_shirt.objects.get(pk=pk)
    similar=T_shirt.objects.order_by('?')[:4]

    context={
    'product':product,'similar':similar
    }
    return render(request,'single.html',context)

def t_shirt_order(request,pk):
    product=T_shirt.objects.get(pk=pk)
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
    'product':product,
    }

    return render(request,'order.html',context)
