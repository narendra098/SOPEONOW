from django.db import models

# Create your models here.
class received_order(models.Model):
    item_name = models.CharField(max_length=50)
    item_cost = models.IntegerField()
    item_quantity = models.IntegerField()
    item_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_stock_alert = models.IntegerField(default=1)
    type = models.CharField(max_length=5)



