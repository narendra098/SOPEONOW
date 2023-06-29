from django.urls import path
from . import views


urlpatterns = [
   
    path('item-list', views.item_list, name='item_list'),
    
    path('create-new-item', views.create_new_item,name='create_new_item'),

     path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),

     path('order_item/<int:item_id>', views.OrderItem, name='order_item'),

     path('sell_item/<int:item_id>', views.SellItem, name='sell_item')

    ]