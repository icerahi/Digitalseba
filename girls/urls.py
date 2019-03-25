from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.girls,name="girls"),
    path('<int:pk>/',views.girls_single,name='girls_single'),
    path('<int:pk>/order',views.girls_order,name='girls_order')

]
