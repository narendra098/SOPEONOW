from django.urls import path
from . import views


urlpatterns = [
   
    path('item-list', views.item_list, name='item_list'),
    
    path('create-new-item', views.create_new_item,name='create_new_item'),

    ]