from django.shortcuts import render
from inventory.models import Item
from django.db.models import Max
from transactions.models import Transaction
from django.db.models import Sum
from django.db.models import F

# Create your views here.
def home(request):
    total_items = Item.objects.count()

    transactions = Transaction.objects.all().order_by('-id')

    total_txn_amount = Transaction.objects.aggregate(total_txn_amount=Sum('transaction_amount'))['total_txn_amount'] or 0.00
    
    total_items_cost = Item.objects.aggregate(total_items_cost=Sum('item_cost'))['total_items_cost'] or 0.00

    profit = total_txn_amount - total_items_cost
    
    highest_cost_item = Item.objects.order_by('-item_cost').first()

    items_stock_alert = Item.objects.filter(item_quantity_left__lte=F('item_stock_alert'))
    
    items = Item.objects.all()
    top_profit_item = None
    max_profit = 0

    for item in items:
        profit = (item.item_selling_price - item.item_cost) * item.item_quantity_sold
        if profit > max_profit:
            max_profit = profit
            top_profit_item = item

   

    print(highest_cost_item.item_name) 
    return render(request,'index.html', 
                  {'total_items':total_items, 
                   'costly_item':highest_cost_item, 
                   'transactions':transactions,
                   'profit':format(profit,','),
                   'sales':format(total_txn_amount,','),
                   'item_stock_alert':items_stock_alert,
                   'top_profit_item':top_profit_item
                   })
