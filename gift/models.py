from django.db import models
from PIL import Image

# Create your models here.
class Gift(models.Model):
    title=models.CharField(max_length=200)
    product_code=models.CharField(max_length=100,blank=True,null=True)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='Gift',default='default.jpg')
    description=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    band=models.CharField(max_length=20,default='hmm,compay')
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
