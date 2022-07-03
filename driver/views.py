from tabnanny import check
from urllib import response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status

# Create your views here.

class DriveruserView(APIView):
    
    def get(self,request,username):
        try:
            user = UserRegister.objects.filter(username = username)
        except:
            return Response({"error":"No data is here"}, status.HTTP_400_BAD_REQUEST)

        serializer = DriveruserView(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class Driverprofile(APIView):
    def get(self, request):
        user = UserRegister.objects.get(username=request.user)
        serializer = UserRegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class passwordChange(APIView):
     def patch(self, request):
        print(request.data)
        user = UserRegister.objects.get(id = request.data['id'] )
        if user.check_password(request.data['password']):
            user.set_password(request.data["newpassword"])
            user.save()
            return Response({"user":"is change password"})
        else:
            return Response({"user":"is Error password"},status=status.HTTP_400_BAD_REQUEST)
        
        

