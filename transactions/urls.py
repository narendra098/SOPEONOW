from django.urls import path
from . import views


urlpatterns = [

    path('show_transactions', views.show_transactions, name='show_transactions'),
    
    ]