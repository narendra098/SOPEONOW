from django.shortcuts import render
from inventory.models import Item
from django.db.models import Max
from transactions.models import Transaction
from django.db.models import Sum

# Create your views here.
def home(request):
    total_items = Item.objects.count()

    transactions = Transaction.objects.all().order_by('-id')

    total_txn_amount = Transaction.objects.aggregate(total_txn_amount=Sum('transaction_amount'))['total_txn_amount'] or 0.00
    
    total_items_cost = Item.objects.aggregate(total_items_cost=Sum('cost'))['total_items_cost'] or 0.00

    profit = total_txn_amount - total_items_cost
    
    highest_cost_item = Item.objects.order_by('-cost').first()
    costly_item= None
    if highest_cost_item:
        costly_item = highest_cost_item
    else:
        costly_item = None


    return render(request,'index.html', 
                  {'total_items':total_items, 
                   'costly_item':costly_item, 
                   'transactions':transactions,
                   'profit':format(profit,','),
                   'sales':format(total_txn_amount,','),
                   })
