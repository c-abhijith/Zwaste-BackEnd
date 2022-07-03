from django.urls import path
from .import views
from .views import *



urlpatterns = [
    
    
    
    path('products',productsView.as_view(),name='productsView'),
    path('products/<int:pk>',productsViewlist.as_view(),name='productsView'),
    path('worker',workerView.as_view(),name='workerView'),
    path('worker/<int:pk>',workerViewlist.as_view(),name='workerView'),
    path('driver',driverView.as_view(),name='driverView'),
    path('driver/<int:pk>/',driverViewlist.as_view(),name='driverView'),
    path('vehicle',vehicleView.as_view(),name='vehicleView'),
    path('vehicle/<int:pk>',vehicleViewlist.as_view(),name='vehicleView'),
    path('todayduty',todayDuty.as_view(),name='duty'),
    path('dutyusers/<int:pk>',todayDutyList.as_view(),name='dutyusers'),
    path('adddriver',addDriver.as_view(),name='adddriver'),
    # path('driverregister/',Driver_register.as_view(),name='adddriver'),

    
    

    
    
]