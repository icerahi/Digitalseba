from django.contrib import admin
from .models import Gift
from rangefilter.filter import DateRangeFilter

# Register your models here.
class Register(admin.ModelAdmin):
    list_display=['title','product_code','price','band','active','date']
    search_fields=['title','product_code','price','band','active','date','description']
    list_filter=(('date',DateRangeFilter),)
    editable_fields=['title','product_code','price','band','active']


admin.site.register(Gift,Register)
