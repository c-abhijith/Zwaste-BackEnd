
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from admins.models import Products
from django.db.models import Q
from rest_framework.decorators import api_view

import razorpay
# from payment import serializer
from .serializer import *
from payment.models import OrderSuccess

# from Back_End.payment.models import OrderSuccess
client = razorpay.Client(auth=("rzp_test_xFSWIL714S4Ayy", "qpHgGRQLtFruIlax45rLXP0M"))


# Create your views here.


class PlaceOrder(APIView):
    def post(self, request):
        print("----------------------------")
        razorpay_order = client.order.create(
            dict(
                amount=request.data["price"] * 100,
                currency="INR",
                payment_capture='0'
            ))
        return Response(razorpay_order, status=status.HTTP_200_OK)


class PlaceOrdersuccess(APIView):

    def post(self,request):
       
        print(type(request.data["product_id"]))
       
        order = Products.objects.get(id = request.data["product_id"])
      
        products = OrderSuccess.objects.create(user_id = request.user,productname = order)
        products.save()
      
        return Response({"sucess":"payment is success"})

class Listoders(APIView):

    def get(self,request):
        try:
            order = OrderSuccess.objects.all()
        except OrderSuccess.DoesNotExist:
            return Response({"error":"Not found"},status=status.HTTP_403_FORBIDDEN)    
        serializer =  OrderSuccessSerializer(order,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Listodersdriver(APIView):
    def get(self,request):
        try:
            order = OrderSuccess.objects.filter(Q(status="Placed"))
        except OrderSuccess.DoesNotExist:
            return Response({"error":"Not found"},status=status.HTTP_403_FORBIDDEN)    
        serializer =  OrderSuccessSerializer(order,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class ListodersdriverList(APIView):
    def get(self, request,pk):   
        
        try:
            order = OrderSuccess.objects.filter(Q(status="Placed"),pk=pk)
        except OrderSuccess.DoesNotExist:
            return Response({"error":"Not found"},status=status.HTTP_403_FORBIDDEN)    
        serializer =  OrderSuccessSerializer(order,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)   

    def patch(self,request,pk):
        print(pk)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
     
        order = OrderSuccess.objects.get(pk=pk)
        order.status="Delivered"
        order.save()
        return Response({"id":"save"})



@api_view(["GET"])
def purchase(request,pk):
    orders = OrderSuccess.objects.filter(user_id = pk)
    serializer =  OrderSuccessSerializer(orders,many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)
