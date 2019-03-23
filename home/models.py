from django.db import models

# Create your models here.
class Order(models.Model):
    product_name=models.CharField(max_length=200)
    product_code=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    customar_name=models.CharField(max_length=100)
    customar_mail=models.CharField(max_length=100)
    customar_phone=models.CharField(max_length=30)
    address=models.CharField(max_length=300,default='example_address')
    customar_city=models.CharField(max_length=300)

    def __str__(self):
        return self.product_name
