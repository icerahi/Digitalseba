from django.db import models
from PIL import Image

# Create your models here.
class Shirt(models.Model):
    title=models.CharField(max_length=200)
    product_code=models.CharField(max_length=100,blank=True,null=True)
    picture=models.ImageField(upload_to='Shirt',default='default.jpg')
    price=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    band=models.CharField(max_length=20,default='sdfv compnay')
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
