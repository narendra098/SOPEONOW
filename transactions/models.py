from django.db import models

# Create your models here.

class Transaction(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=4)

    def __str__(self):
        return self.item_name

