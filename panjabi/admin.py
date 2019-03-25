from django.contrib import admin
from .models import Panjabi
# Register your models here.
from rangefilter.filter import DateRangeFilter
class Register(admin.ModelAdmin):
    list_display=['title','product_code','price','band','active','date']
    search_fields=['title','product_code','price','band','active','date','description']
    list_filter=(('date',DateRangeFilter),)
    editable_fields=['title','product_code','price','band','active']

admin.site.register(Panjabi,Register)
