from django.shortcuts import get_object_or_404, redirect, render
from . models import Item
from .forms import ItemForm
from transactions.models import Transaction
from decimal import Decimal

# Create your views here.

finance = {'profit':0, 'revenue':0}

def item_list(request):
    
    items = Item.objects.all()        
    context = {'items':items, 'form':None} 
    
    
    if request.method == 'POST':
      
        if request.POST.get('form_type') == 'sell_item_form':
            
            transaction = Transaction()
            item_id = request.POST['sell_item_id']
            item = Item.objects.get(id=item_id)
            transaction.item_id = item_id
            transaction.item_name = item.name
            transaction.item_selling_price = item.selling_price
            transaction.number_of_items = Decimal(request.POST['number_of_items'])
            transaction.transaction_amount = Decimal(item.selling_price)*(transaction.number_of_items)
            transaction.transaction_type = request.POST['transaction_type']
            transaction.save()
            item.quantity = item.quantity - transaction.number_of_items
        
            item.quantity_sold += transaction.number_of_items
            item.save()

        elif request.POST.get('form_type') == 'edit_item_form':
            
            item_id = request.POST['edit_item_id']
            item = Item.objects.get(id = item_id)
            form = ItemForm(request.POST, instance=item)
            print(context)
            context['form'] = form
            
            item.name = request.POST['item_name']
            item.cost = request.POST['item_cost']
            item.quantity = request.POST['item_quantity']
            item.quantity_sold = request.POST['quantity_sold']
            item.selling_price = request.POST['selling_price']
            item.save()

     
   
    
    
    return render(request, 'items-list.html', context)



def create_new_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():

        item = form.save()
        print(form.cleaned_data)
       

        item_id = item.id
        item_name = item.name
        item_quantity = item.quantity
        item_selling_price = item.selling_price
        amount = item_quantity*item_selling_price
        
        transaction = Transaction(
                        item_id=item_id, 
                        item_name=item_name, 
                        item_selling_price=item_selling_price, 
                        number_of_items = item_quantity,
                        transaction_amount = amount, 
                        transaction_type = 'buy'
                        )
        
        transaction.save()

        
        return redirect('/create-new-item')



    context = {'form':form}

    return render(request,'create-new-item.html', context)

