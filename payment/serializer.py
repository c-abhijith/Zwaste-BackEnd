from rest_framework import serializers
from admins.serializer import productSerializer
from user.serializers import UserRegisterSerializer
from .models import *




class OrderSuccessSerializer(serializers.ModelSerializer):
    
    productname = productSerializer()
    user_id = UserRegisterSerializer()


    class Meta :
        model = OrderSuccess
        fields = "__all__"
