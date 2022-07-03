from dataclasses import field
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserRegister
        fields = "__all__"
        
    def create(self,validated_data):
        user = UserRegister.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            phone_number =validated_data['phone_number'],
            long =validated_data['long'],
            lat =validated_data['lat'],
            place =validated_data['place'],
            District =validated_data['District'],
            State=validated_data['State'],
            Country=validated_data['Country'],
            
            


        )
        user.set_password(validated_data['password'])
        print(user)
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        # ...
        return token


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserRegister
        fields="__all__"

class WastefullSerilizer(serializers.ModelSerializer):
    userid = UserRegisterSerializer()
    class Meta:
        model = Wastefullcall
        fields = ["userid"]
