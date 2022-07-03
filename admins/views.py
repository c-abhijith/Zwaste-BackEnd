
from lib2to3.pgen2.driver import Driver
from django import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Q
from rest_framework import viewsets


# Create your views here.
class Driver_register(viewsets.ModelViewSet):
    queryset = UserRegister.objects.filter(Q(is_superuser=False) & Q(is_staff=True)).order_by('-date_joined')
    serializer_class = DriverRegistrationfirstSerializer

   
     

class productsView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request):
        print("==============================================")
        try:
            products = Products.objects.all()
            serializer = productSerializer(products,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK) 

        except Products.DoesNotExist:
            return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN)   

    def post(self,request, format=None):
        print(request.data)
        a = dict(request.data)
        print(a)
        print(";;;;;;;;;;;;;;;;;;;;;;;;;")
        data = {
            'description':a['description'][0],
            'name': a['name'][0],
            'price': int(a['price'][0]),
            'image': a['image'][0],
        }

        
        
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            

class productsViewlist(APIView):

    def get(self,request,pk):
        try:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(pk)
            product = Products.objects.get(id = pk)
            serializer = productSerializer(product,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({"error":"This product is not exists"},status=status.HTTP_403_FORBIDDEN)    


    def put(self,request,pk):
        product = Products.objects.get(pk=pk)
        serializer = productSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        product = Products.objects.filter(id = pk).delete()
        # print(product)
        # print("ppppppppppppppppppppppp")
        # product.delete()
        # serializer=productSerializer(product,data = request.data)
        return Response(status=status.HTTP_200_OK)

 
class workerView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request):
        try:
            worker = Workers.objects.all()
            serializer = workerSerializer(worker,many = True)
            return Response(serializer.data)
        except Workers.DoesNotExist:
            return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN)
    
    def post(self,request,format = None):
        print(request.data)
        workers_datas = dict(request.data)
        
        data = {
                   'Address':workers_datas['Address'][0],
                    'Name': workers_datas['Name'][0],
                    'phone_number': int(workers_datas['phone_number'][0]),
                    'worker_Image': workers_datas['worker_Image'][0],   
                }
        serializer = workerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            

class workerViewlist(APIView):

    def get(self,request,pk):
        worker = Workers.objects.get(id = pk)
        serializer = workerSerializer(worker)
        return Response(serializer.data)


    def put(self,request,pk):
        print(pk,"^^^^^^^^^^^^^^^^^^^^^^^")
        worker = Workers.objects.get(pk=pk)
        serializer = workerSerializer(worker,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    def delete(self,request,pk):
        worker = Workers.objects.get(pk = pk).delete() 
        return Response(status=status.HTTP_200_OK)       
        



class driverView(APIView):

    def get(self,request):
        try:
            driver = DriverRegistration.objects.all()
        except DriverRegistration.DoesNotExist:
            return Response({'error':"Not found"},status=status.HTTP_403_FORBIDDEN)    
        serializer = DriverRegistrationSerializer(driver,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DriverRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
        else:
            return Response(serializer.errors)    
            

class driverViewlist(APIView):

    def get(self,request,pk):
        driver = DriverRegistration.objects.get(id = pk)
        serializer = DriverRegistrationSerializer(driver)
        return Response(serializer.data)


    def put(self,request,pk):
        print(pk,"+++++++++++++++===")
        print(request.data,"ddddddddddddddddddd")
        driver = DriverRegistration.objects.get(pk=pk)
        serializer = DriverRegistrationSerializer(driver,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    def delete(self,request,pk):


        serializer = DriverRegistrationSerializer(pk)

        print(serializer)

        dr_id = DriverRegistration.objects.get(id= pk)

        user = UserRegister.objects.get(id=dr_id.Drivename.id)
        user.is_staff = False
        user.save()


        DriverRegistration.objects.get(pk = pk).delete()
        return Response(status=status.HTTP_200_OK)  



class vehicleView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request):
        try:
            vehicle = Vehicles.objects.all()
            serializer = vehicleSerializer(vehicle,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Vehicles.DoesNotExist:
            return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN)

    def post(self,request):
        vehicle_data = dict(request.data)
        data = {
            'vehicle_RCowner':vehicle_data['vehicle_RCowner'][0],
            'vehicle_Name': vehicle_data['vehicle_Name'][0],
            'vehicle_number': int(vehicle_data['vehicle_number'][0]),
            'vehicleBook_image': vehicle_data['vehicleBook_image'][0],
            
        }

        serializer = vehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            

class vehicleViewlist(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request,pk):
        vehicle = Vehicles.objects.get(id = pk)
        serializer = vehicleSerializer(vehicle)
        return Response(serializer.data)


    def put(self,request,pk):
        print(pk,"llllllllllllllllllllllllll")
        print(request.data,"}}}}}}}}}}}}]")
        vehicle = Vehicles.objects.get(pk=pk)
        serializer = vehicleSerializer(vehicle,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    def delete(self,request,pk):
       
        Vehicles.objects.get(pk = pk).delete() 
        return Response(status=status.HTTP_200_OK)        


class todayDuty(APIView):

    def get(self,request):
        try:

            Users = Todaywork.objects.all()
            serializer = TodayworkSerilizer(Users,many = True)
            return Response(serializer.data)
        
        except Todaywork.DoesNotExist:
            return Response({"error":"This Users is not exists"},status=status.HTTP_403_FORBIDDEN)


    def post(self, request):
        print(request.data,"______________d____________________")
        # todayworks = dict(request.data)
      
        print(int(request.data['Driver']),"________#__________")
        print(int(request.data['users']),"____________3________")
        Driver = UserRegister.objects.get(pk=int(request.data['Driver']))
        users = UserRegister.objects.get(pk=int(request.data['users']))
        Today = Todaywork.objects.create(Driver=Driver,users=users)
        serializer = TodayworkSerilizer(data=request.data)
        return Response({"error":"This Users is not exists"})
        # print(serializer,"-------------------------------")
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)

        # else:_
        #     print(serializer.errors)
        #     print("--------Error----------")
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


class todayDutyList(APIView):
    def get(self, request,pk):
        print(pk,"----------------------------")
        vehicle = Todaywork.objects.filter(Driver__id = pk)
        # print(vehicle,"ppppppppppppppppppp")
        

        serializer = TodayworkSerilizer(vehicle,many = True)
        return Response(serializer.data)


#     def get(self, request):
#         try:
        
#             Drivers = UserRegister.objects.filter(
#                 Q(is_superuser=0) & Q(is_staff=1)).order_by('-date_joined')
#             out=[]
#             dic={}
#             for i in Drivers:
#                 users=DriverRegistration.objects.filter(Drivename__id=i.id)
#                 dic['driver']=i.username
#                 dic['pass']=[j.Listusers.username for j in users]
#                 out.append(dic)
#                 dic={}
#             print(dic)
#         except UserRegister.DoesNotExist:
#             return Response({'error': "Not found"}, status=status.HTTP_403_FORBIDDEN)
#         # print(users)
#         serializer = UserRegisterSerializer(Drivers, many=True)
#         return Response(out, status=status.HTTP_200_OK)

class addDriver(APIView): 
    def get(self, request):
            try:
                Filter = [i.users.id for i in Todaywork.objects.all()]
                print(Filter)

                

                print("++++++++++++++++")
                users = UserRegister.objects.filter(
                        Q(is_superuser=0) & Q(is_staff=0) & ~Q( id__in = Filter)).order_by('-date_joined')
            except UserRegister.DoesNotExist:
                return Response({'error': "Not found"}, status=status.HTTP_403_FORBIDDEN)
            print(users)
            serializer = UserRegisterSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)