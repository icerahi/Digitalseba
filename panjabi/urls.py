from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.panjabi,name="panjabi"),
    path('<int:pk>',views.panjabi_single,name='panjabi_single'),
    path('<int:pk>/order',views.panjabi_order,name='panjabi_order')

]
