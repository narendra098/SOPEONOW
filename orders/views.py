from django.shortcuts import render
from transactions.models import Transaction
from inventory.models import Item
from . models import received_order
from decimal import Decimal

# view for orders placed page
def orders_placed(request):

    orders = received_order.objects.all()
    context = {'orders':orders}
    
    if request.method == 'POST':
        # if i click receive button then increasing the item quantity
        if request.POST.get('btn_type') == 'received_order':
            print(request.POST)
            order_id = request.POST['order_id']
            item_id = request.POST['order_item_id']
            item_name = request.POST['item_name']
            item_cost = request.POST['item_cost']
            quantity = request.POST['quantity']
            
            # increasing item quantity
            item = Item.objects.get(id=item_id)
            item.item_quantity += int(quantity)
            item.save()    
            
            # pushing data to transaction model with type as 'received'
            transaction = Transaction(
                item_id = item_id,
                item_name = item_name,
                item_cost = item_cost,
                item_quantity = quantity,
                transaction_amount = Decimal(quantity)*Decimal(item_cost),
                transaction_type = 'received'
            )

            transaction.save()

            # once clicked on receive increasing the item amount then deleting the placed order for not getting confusion
            order = received_order.objects.get(id=order_id)
            order.delete()            

        # on clicking cancel 
        elif request.POST.get('btn_type') == 'cancel_order':
            print(request.POST)
            order_id = request.POST['order_id']
            item_id = request.POST['order_item_id']
            item_name = request.POST['item_name']
            item_cost = request.POST['item_cost']
            quantity = request.POST['quantity']
  
   # pushing data to transaction model with type as 'cancelled'
            transaction = Transaction(
                item_id = order_id,
                item_name = item_name,
                item_cost = item_cost,
                item_quantity = quantity,
                transaction_amount = Decimal(quantity) * Decimal(item_cost),
                transaction_type = 'cancelled'
            )
            transaction.save()
          # once clicked on cancel order, deleting the placed order for not getting confusion
            order = received_order.objects.get(id=order_id)
            order.delete()
     
    return render(request, 'orders_placed.html', context)

 
# view for showing all received orders  
def received_orders(request):

    orders_received = Transaction.objects.filter(transaction_type = 'received')

    context = {'orders_received':orders_received}

    return render(request, 'orders_received.html', context)

# view for all cancelled orders
def cancelled_orders(request):

    orders_cancelled = Transaction.objects.filter(transaction_type = 'cancelled')

    context = {'orders_cancelled': orders_cancelled}

    return render(request, 'orders_cancelled.html', context)

