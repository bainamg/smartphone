from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Brand(models.Model):
    Name=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    Image=models.ImageField(upload_to ='static/image/brand')


class PhoneModels(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    votes = models.IntegerField(null=True)
    release_year=models.IntegerField(null=True)
    available_quatities=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    count=models.IntegerField(null=True)
    is_available=models.BooleanField(null=True)
    Image=models.ImageField(upload_to='static/image/models') 


class Transactions(models.Model):
    Transaction_choice=[
        ('Card',"1"),
        ('Cash',"2")
    ]
    
    User=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Model= models.ForeignKey(PhoneModels, on_delete=models.CASCADE)
    Transaction_type=models.CharField(max_length=200,choices=Transaction_choice,null=True,blank=True)
    Amount= models.IntegerField(null=True)


