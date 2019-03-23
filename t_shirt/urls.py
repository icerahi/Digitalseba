from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.t_shirt,name="t_shirt"),
    path('<int:pk>/',views.t_shirt_single,name='t_shirt_single'),
    path('<int:pk>/order',views.t_shirt_order,name='t_shirt_order')

]
