from django.shortcuts import render
from transactions.models import Transaction
from inventory.models import Item
from . models import received_order

# Create your views here.
def orders_placed(request):

    transactions = Transaction.objects.all()
    context = {'transactions':transactions}

    if request.method == 'POST':
        if request.POST.get('btn_type') == 'received_order':
            print(request.POST)
            txn_id = request.POST['transaction_id']
            item_name = request.POST['item_name']
            item_selling_price = request.POST['item_selling_price']
            txn_amount = request.POST['amount']
            quantity = request.POST['quantity']

            order = received_order(txn_id=txn_id, item_name = item_name, item_selling_price= item_selling_price, txn_amount=txn_amount, quantity = quantity, order_type='received')
            order.save()
            
        elif request.POST.get('btn_type') == 'cancel_order':
            print(request.POST)
            txn_id = request.POST['transaction_id']
            item_name = request.POST['item_name']
            item_selling_price = request.POST['item_selling_price']
            txn_amount = request.POST['amount']
            quantity = request.POST['quantity']
            order = received_order(txn_id=txn_id, item_name = item_name, item_selling_price= item_selling_price, txn_amount=txn_amount, quantity = quantity, order_type='cancelled')
            order.save()

            txn = Transaction.objects.get(id=txn_id)
            item_id = txn.item_id
            item = Item.objects.get(id=item_id)
            item.delete()
            

    return render(request, 'orders_placed.html', context)

 
def received_orders(request):

    orders_received = received_order.objects.filter(order_type = 'received')

    context = {'orders_received':orders_received}

    return render(request, 'orders_received.html', context)

def cancelled_orders(request):

    orders_cancelled = received_order.objects.filter(order_type = 'cancelled')

    context = {'orders_cancelled': orders_cancelled}

    return render(request, 'orders_cancelled.html', context)

