from django.db import models
from PIL import Image
# Create your models here.

class Pant(models.Model):
    title=models.CharField(max_length=100)
    product_code=models.CharField(max_length=100)
    picture=models.ImageField(upload_to="Pant",default='default.jpg')
    description=models.TextField()
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    band=models.CharField(max_length=20,default='d comanpy')
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
