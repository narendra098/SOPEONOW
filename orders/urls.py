from django.urls import path
from . import views


urlpatterns = [
   # url for orders placed page
    path('orders_placed', views.orders_placed, name='orders_placed'),
    #url for orders received page
    path('orders_received', views.received_orders, name='received_orders'),
    #url for orders cancelled page
   path('orders_cancelled', views.cancelled_orders, name='cancelled_orders'),
    ]