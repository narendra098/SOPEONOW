from django.shortcuts import render

from .models import Transaction

# view for showing all transactions
def show_transactions(request):
    transactions = Transaction.objects.all()
    context = {'transactions':transactions}
    return render(request, 'transactions.html',context)
