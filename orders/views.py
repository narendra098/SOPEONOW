from django.shortcuts import render
from transactions.models import Transaction
from inventory.models import Item
from . models import received_order
from decimal import Decimal

# Create your views here.
def orders_placed(request):

    orders = received_order.objects.all()
    context = {'orders':orders}
    
    if request.method == 'POST':
        if request.POST.get('btn_type') == 'received_order':
            print(request.POST)
            order_id = request.POST['order_id']
            item_name = request.POST['item_name']
            item_cost = request.POST['item_cost']
            item_selling_price = request.POST['item_selling_price']
            quantity = request.POST['quantity']

            item = Item(item_id= order_id, 
                         item_name=item_name, 
                         item_cost=item_cost, 
                         item_quantity_left=quantity,
                         item_selling_price=item_selling_price,
                         item_quantity_sold = 0,
                         )
            item.save()

            transaction = Transaction(
                item_id = order_id,
                item_name = item_name,
                item_cost = item_cost,
                item_quantity = quantity,
                transaction_amount = Decimal(quantity)*Decimal(item_cost),
                transaction_type = 'received'
            )

            transaction.save()
            order = received_order.objects.get(id=order_id)
            order.delete()            


        elif request.POST.get('btn_type') == 'cancel_order':
            print(request.POST)
            order_id = request.POST['order_id']
            item_name = request.POST['item_name']
            item_cost = request.POST['item_cost']
            item_selling_price = request.POST['item_selling_price']
            quantity = request.POST['quantity']

            print(type(quantity))
            print(type(item_cost))

            order = received_order.objects.get(id=order_id)
            order.delete()

            transaction = Transaction(
                item_id = order_id,
                item_name = item_name,
                item_cost = item_cost,
                item_quantity = quantity,
                transaction_amount = Decimal(quantity) * Decimal(item_cost),
                transaction_type = 'cancelled'
            )

            transaction.save()
     
            

    return render(request, 'orders_placed.html', context)

 
def received_orders(request):

    orders_received = Transaction.objects.filter(transaction_type = 'received')

    context = {'orders_received':orders_received}

    return render(request, 'orders_received.html', context)

def cancelled_orders(request):

    orders_cancelled = Transaction.objects.filter(transaction_type = 'cancelled')

    context = {'orders_cancelled': orders_cancelled}

    return render(request, 'orders_cancelled.html', context)

