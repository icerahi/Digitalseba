from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.nitto,name="nitto"),
    path('<int:pk>/',views.nitto_single,name='nitto_single'),
    path('<int:pk>/order',views.nitto_order,name='nitto_order')

]
