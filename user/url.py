from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from .import views
from .views import *



urlpatterns = [
    
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',user_register.as_view(),name='user_register'),
    path('register/<int:pk>',user_list.as_view(),name='user_list'),
    path('registeradddriver/<int:pk>',user_listadddriver.as_view(),name='user_list'),
    path('userprofile',UserProfile.as_view(),name='user_profile'),
    path('profile/<int:pk>',profile.as_view(),name='profile'),
    path('usersdriver',userDriver.as_view(),name='usersdriver'),
    path('usersdriver/<int:pk>',userDrivers.as_view(),name='usersdriver'),
    path('wastefull/<int:pk>',Wastefull.as_view(),name='wastefull'),
    path('wastefull',Wasteful.as_view(),name='wastefull'),
    

    









    
    
]