from django.urls import path
from .import views
from .views import *




urlpatterns = [
      path('products/<str:username>',DriveruserView.as_view(),name='DriveruserView'),
      path('driverprofile',Driverprofile.as_view(),name='driverprofile'),
      path('passwordChange',passwordChange.as_view(),name='passwordChange'),
      

  

]