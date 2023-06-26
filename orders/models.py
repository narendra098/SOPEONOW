from django.db import models

# Create your models here.
class received_order(models.Model):
    txn_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    txn_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=15)

