
from django.urls import path
from .import views



urlpatterns = [
    path('payment', views.PlaceOrder.as_view()),
    path('payment/success', views.PlaceOrdersuccess.as_view()),
    path('listoders', views.Listoders.as_view()),
    path('listodersdriver', views.Listodersdriver.as_view()),
    path('listodersdriver/<int:pk>', views.ListodersdriverList.as_view()),
    path('purchase/<int:pk>', views.purchase,name='')

]

