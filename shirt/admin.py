from django.contrib import admin
from .models import Shirt
from rangefilter.filter import DateRangeFilter

# Register your models here.
class Register(admin.ModelAdmin):
    list_display=['title','price','date']
    

admin.site.register(Shirt,Register)
