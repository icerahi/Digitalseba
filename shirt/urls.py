from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.shirt,name="shirt"),
    path('<int:pk>/',views.shirt_single,name='shirt_single'),
    path('<int:pk>/order',views.shirt_order,name='shirt_order')

]
