

from concurrent.futures.process import _python_exit
from functools import partial
from re import U
from django.forms import PasswordInput
from rest_framework import serializers
from .models import *
from user.serializers import UserRegisterSerializer







class DriverRegistrationfirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = "__all__"

    def create(self,validated_data):
        user = UserRegister.objects.create(
            username = validated_data['username'],
            phone_number =validated_data['phone_number'],
            is_staff = True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        

                






class productSerializer(serializers.ModelSerializer):
    

    class Meta :
        model = Products
        fields = ["id","name","description","price","image"]


class workerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workers
        fields = '__all__'


class DriverRegistrationSerializer(serializers.ModelSerializer):
    Drivename = UserRegisterSerializer()
    
    class Meta:
        model = DriverRegistration
        fields = '__all__'   


class vehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = '__all__'   


class TodayworkSerilizer(serializers.ModelSerializer):
    Driver = UserRegisterSerializer(partial=True)
    users = UserRegisterSerializer(partial = True)
    class Meta:
        model = Todaywork
        fields= '__all__'




