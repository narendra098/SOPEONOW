from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from . models import Item
from . forms import *
from transactions.models import Transaction
from orders.models import received_order


#view for rendering items list
def item_list(request):
    
    items = Item.objects.all()        
    context = {'items':items} 
 
    return render(request, 'items-list.html', context) 


# view for creating new item
def create_new_item(request):
    form = CreateNewItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()     
        return redirect('/create-new-item')

    context = {'form':form}

    return render(request,'create-new-item.html', context)


# view for editing item details
def edit_item(request, item_id):
  
    item = Item.objects.get(id=item_id)
    
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



# view for ordering quantity for an item
def OrderItem(request, item_id):

    item = Item.objects.get(id=item_id)

    form = OrderItemForm(instance=item)

    context = {'form':form}

    if request.method =='POST':
        
        form = OrderItemForm(request.POST, instance=item)

        if form.is_valid():
            item_id = item_id
            item_quantity = form.cleaned_data['order_item_quantity']
            item_name = form.cleaned_data['item_name']
             
            #if form is valid pushing data into received orders  model
            order = received_order(
                item_id =item_id,
                item_name = item_name,
                item_cost = item.item_cost,
                item_quantity = item_quantity,
            )
            order.save()

            # then pushing data to transaction model with transaction type as buy, because we are buying(ordering) the item
            transaction = Transaction(
                item_id = item_id,
                item_name = item_name,
                item_cost = item.item_cost,
                item_quantity = item_quantity,
                transaction_amount = Decimal(item_quantity)*Decimal(item.item_cost),
                transaction_type = 'buy'
            )
            transaction.save()       

     
            return redirect('/item-list')
    


    return render(request, 'order_item.html', context)


#view for selling an item with it's quantity
def SellItem(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = SellItemForm(request.POST)

        if form.is_valid():
            item_quantity_selling = form.cleaned_data['item_quantity_selling']

            # if form is valid decreasing the item quantity
            if item_quantity_selling <= item.item_quantity:
                item.item_quantity -= item_quantity_selling
                item.save()
                    #then pushing data to transaction model with transaction type as 'sold'
                transaction = Transaction(
                item_id = item_id,
                item_name = item.item_name,
                item_cost = item.item_cost,
                item_quantity = item_quantity_selling,
                transaction_amount = Decimal(item_quantity_selling)*Decimal(item.item_selling_price),
                transaction_type = 'sold'
                )
                transaction.save()


                return redirect('/item-list')
                
            else:
                form.add_error('item_quantity_selling', "Quantity selling cannot be greater than available quantity.")
    else:
        form = SellItemForm(initial={
            'item_id': item.id,
            'item_name': item.item_name,
            'item_quantity': item.item_quantity,
        })

    context = {'form': form}
    return render(request, 'sell-item.html', context)
  
# view for showing all sold items   
def sold_items(request):
    # getting all the sold items from transaction model
    items_sold = Transaction.objects.filter(transaction_type='sold')

    context = {'items_sold':items_sold}

    return render(request, 'items-sold.html', context)
