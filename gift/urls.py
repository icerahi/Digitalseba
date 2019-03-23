from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.gift,name="gift"),
    path('<int:pk>/',views.gift_single,name='gift_single'),
    path('<int:pk>/order',views.gift_order,name='gift_order')
]
