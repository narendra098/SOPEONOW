from django.shortcuts import get_object_or_404, redirect, render
from . models import Item
from . forms import *
from transactions.models import Transaction




# Create your views here.



def item_list(request):
    
    items = Item.objects.all()        
    context = {'items':items} 
 
    return render(request, 'items-list.html', context) 



def create_new_item(request):
    form = CreateNewItemForm(request.POST or None)

    if form.is_valid():

        order = form.save()
      
        order_id = order.id
        item_name = order.item_name
        item_cost = order.item_cost
        item_quantity = order.item_quantity
        item_selling_price = order.item_selling_price
        amount = item_quantity*item_selling_price
        
        
        transaction = Transaction(
                        item_id=order_id, 
                        item_name=item_name, 
                        item_cost = item_cost, 
                        item_quantity = item_quantity,
                        transaction_amount = amount, 
                        transaction_type = 'received'
                        )
        
        transaction.save()

        
        return redirect('/create-new-item')



    context = {'form':form}

    return render(request,'create-new-item.html', context)



def edit_item(request, item_id):
  
    item = Item.objects.get(item_id=item_id)
    
    form = EditItemForm(instance=item)  

 
    context = {'form':form, 'error':''}

    
 
    if request.method == 'POST':

        

        form = EditItemForm(request.POST, instance=item)
    
        if form.is_valid():
            form.save()
            return redirect('/item-list')
        else:
            print(form.errors) 
            
            context['error'] = form.errors
    
    return render(request, 'edit_item.html', context)



def OrderItem(request, item_id):

    item = Item.objects.get(item_id=item_id)

    form = OrderItemForm(instance=item)

    context = {'form':form}

    if request.method =='POST':
        
        form = OrderItemForm(request.POST, instance=item)

        if form.is_valid():
            order_item_quantity = form.cleaned_data['order_item_quantity']
            item.item_quantity_left += order_item_quantity
            item.save()
            form.save()
            return redirect('/item-list')
    


    return render(request, 'order_item.html', context)


def SellItem(request, item_id):
    item = Item.objects.get(item_id=item_id)

    if request.method == 'POST':
        form = SellItemForm(request.POST)

        if form.is_valid():
            item_quantity_selling = form.cleaned_data['item_quantity_selling']
            
            if item_quantity_selling <= item.item_quantity_left:
                item.item_quantity_left -= item_quantity_selling
                item.save()
                return redirect('/item-list')
                
            else:
                form.add_error('item_quantity_selling', "Quantity selling cannot be greater than available quantity.")
    else:
        form = SellItemForm(initial={
            'item_id': item.item_id,
            'item_name': item.item_name,
            'item_quantity_left': item.item_quantity_left,
        })

    context = {'form': form}
    return render(request, 'sell-item.html', context)
  

