from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.pant,name="pant"),
    path('<int:pk>/',views.pant_single,name='pant_single'),
    path('<int:pk>/order',views.pant_order,name='pant_order')

]
