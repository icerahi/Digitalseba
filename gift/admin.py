from django.contrib import admin
from .models import Gift
from rangefilter.filter import DateRangeFilter

# Register your models here.
class Register(admin.ModelAdmin):
    list_display=['title','price','active','date']
    list_editable =['active','price']


admin.site.register(Gift,Register)
