from rest_framework import serializers
from  user.models import *
from user.serializers import UserRegisterSerializer





class DriveruserSerializer(serializers.ModelSerializer):
    

    class Meta :
        model = UserRegister
        fields = ["id","username"]
