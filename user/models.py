from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser

# from user.models import *
# Create your models here.




class UserRegister(AbstractUser):
    phone_number = models.CharField(max_length=12,null=True)
    long = models.DecimalField(max_digits=20, decimal_places=18,null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=18,null=True)
    value = models.IntegerField(default=False,null=True)
    place = models.CharField(max_length=30,null=True)
    District = models.CharField(null=True,max_length=30)
    State = models.CharField(max_length=30,null=True)
    Country = models.CharField(max_length=20,null=True)

    

    


# class Product(models.Model):

#     name = models.CharField(max_length= 20)
#     description = models.CharField(max_length=50)
#     image = image = models.ImageField(blank=False,upload_to="media/")  
# 
#  

class Wastefullcall(models.Model):
    
    userid= models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    





  

