from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from admins.models import DriverRegistration
from .serializers import *
from rest_framework import status
from django.db.models import Q
from admins.models import Todaywork
from admins.serializer import TodayworkSerilizer
from geopy.geocoders import Nominatim

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class user_register(APIView):

    def get(self, request):
        try:
            print("++++++++++++++++")
            users = UserRegister.objects.filter(
                is_superuser=0 , is_staff=0).order_by('-date_joined')
        except UserRegister.DoesNotExist:
            return Response({'error': "Not found"}, status=status.HTTP_403_FORBIDDEN)
        print(users)
        serializer = UserRegisterSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        geoLoc = Nominatim(user_agent="GetLoc")
        serializer = UserRegisterSerializer(data=request.data)
      
        
        # locname = geoLoc.reverse(str(request.data["lat"])+","+str(request.data['long']))
        # print(locname)
        # print(locname["state"],"====================4444444444444444444=====================")

        if serializer.is_valid():   
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_200_OK)
            

        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_list(APIView):

    def get(self, request, pk):
        try:

            users = UserRegister.objects.get(pk=pk)
            serializer = UserRegisterSerializer(users)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserRegister.DoesNotExist:
            return Response({"error": "This user didn't exist"})

    def patch(self, request, pk):
        user = UserRegister.objects.get(pk=pk)
        user.is_active = not(user.is_active)
        user.save()
        return Response({'user_id': user.id})

class user_listadddriver(APIView):

    def get(self, request, pk):
        try:

            users = UserRegister.objects.get(pk=pk)
            serializer = UserRegisterSerializer(users)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserRegister.DoesNotExist:
            return Response({"error": "This user didn't exist"})

    def patch(self, request, pk):
        
        user = UserRegister.objects.get(pk=pk)
        user.is_staff = True
        print("sample--------")
        user.save()
        print("__________________________")
        DriverRegistration.objects.create(Drivename=user)
        print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLl")
        return Response({'user_id': user.id})
        

class profile(APIView):
    def get(self, request, pk):
        user = UserRegister.objects.get(pk=pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = UserRegister.objects.get(pk=pk)
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


class UserProfile(APIView):
    def get(self, request):
        user = UserRegister.objects.get(username=request.user)
        serializer = UserRegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class userDriver(APIView):
    def get(self, request):
        user = UserRegister.objects.get(username=request.user)
        serializer = UserRegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

        
class userDrivers(APIView):
    def get(self, request,pk):
        user = Todaywork.objects.filter(users__id = pk)

        serializer = TodayworkSerilizer(user,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)        


class Wastefull(APIView):
    def get(self, request, pk):
        

        
        user = Wastefullcall.objects.get(userid = pk)
        serializers = WastefullSerilizer(user)
        
        return Response(serializers.data, status=status.HTTP_200_OK)
       


    def patch(self, request, pk):
        user = UserRegister.objects.get(id=pk) 
        print(user.id,";;;;;;;;;;;;;;;;")
        Wastefullcall.objects.create(userid = user)
        return Response({'user': "Basket is full"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        print(pk,"dddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        Wastefullcall.objects.get(userid = pk).delete() 
        return Response(status=status.HTTP_200_OK)        



class Wasteful(APIView):
    def get(self, request):
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
 
            wasteNotification = Wastefullcall.objects.all()
            print("lllll")
        except:
            print("mmmmmmmmmmmmmmmmm")
            return Response({'error': "Not found"}, status=status.HTTP_403_FORBIDDEN)
        print("oooooooooooo")    
        serializers = WastefullSerilizer(wasteNotification,many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)