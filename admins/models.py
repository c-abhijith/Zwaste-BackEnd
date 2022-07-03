from django.db import models
from user.models import UserRegister
# Create your models here.




class DriverRegistration(models.Model):
    Drivename=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    
    



class Products(models.Model):

    name = models.CharField(max_length= 20)
    description = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image =  models.ImageField(blank=False,upload_to="media")    


class Workers(models.Model):
    worker_Image = models.ImageField(blank=False,upload_to='worker_Image')
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)



class Vehicles(models.Model):
    
    vehicleBook_image = models.ImageField(blank=True,upload_to='Drivers_image')  
    vehicle_Name = models. CharField(max_length=50)
    vehicle_RCowner= models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=15)    

    


class Purchases(models.Model):
    user = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    total = models.CharField(max_length=10)


class Todaywork(models.Model):
    users = models.ForeignKey(UserRegister,on_delete=models.CASCADE,related_name="Username")
    Driver = models.ForeignKey(UserRegister,on_delete=models.CASCADE,related_name="Drivername")
