from django.contrib import admin
from .models import Order
from rangefilter.filter import DateRangeFilter
# Register your models here.
class Register(admin.ModelAdmin):
    list_display=['product_name','price','customar_name','customar_phone']
admin.site.register(Order,Register)
