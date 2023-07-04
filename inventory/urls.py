from django.urls import path
from . import views


urlpatterns = [
   
    #url for items list page
    path('item-list', views.item_list, name='item_list'), 

    #url for create new item
    path('create-new-item', views.create_new_item,name='create_new_item'),
    
     #url for editing item
     path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),
     
     #url for ordering item
     path('order_item/<int:item_id>', views.OrderItem, name='order_item'),
     
     #url for selling item
     path('sell_item/<int:item_id>', views.SellItem, name='sell_item')

    ]