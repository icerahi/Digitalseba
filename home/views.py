from django.shortcuts import render
from django.http import HttpResponse
from gift.models import Gift
from nitto.models import Nitto
from panjabi.models import Panjabi
from pant.models import Pant
from shirt.models import Shirt
from t_shirt.models import T_shirt
# Create your views here.

def home(request):
    gift=Gift.objects.order_by('?')[:4]
    nitto=Nitto.objects.order_by('?')[:4]
    panjabi=Panjabi.objects.order_by('?')[:4]
    pant=Pant.objects.order_by('?')[:4]
    shirt=Shirt.objects.order_by('?')[:4]
    t_shirt=T_shirt.objects.order_by('?')[:4]

    context={'title':'home',
     'gift':gift,
     'nitto':nitto,
     'panjabi':panjabi,
     'pant':pant,
     'shirt':shirt,
     't_shirt':t_shirt,
    }
    return render(request,'home.html',context)
