from django.urls import path
from . import views


urlpatterns = [
   
    path('orders_placed', views.orders_placed, name='orders_placed'),
    path('orders_received', views.received_orders, name='received_orders'),
   path('orders_cancelled', views.cancelled_orders, name='cancelled_orders'),
    ]