from django.db import models
from admins.models import Products
from user.models import UserRegister



# Create your models here.


class OrderSuccess(models.Model):
    user_id = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    productname = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField( max_length=100,default='Placed')