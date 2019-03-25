from django.contrib import admin
from .models import Order
from rangefilter.filter import DateRangeFilter
# Register your models here.


class Register(admin.ModelAdmin):
    list_display=['product_name','product_code','price','quantity','customar_name','customar_mail',
                 'customar_phone','address','customar_city','ordered_date' ]

    search_fields=['product_name','product_code','price','quantity','customar_name','customar_mail',
                 'customar_phone','address','customar_city','ordered_date' ]
    list_filter=(('ordered_date',DateRangeFilter),)


admin.site.register(Order,Register)

admin.site.site_title="BD Digital Seba";
admin.site.site_header="Team IceCream Production";
