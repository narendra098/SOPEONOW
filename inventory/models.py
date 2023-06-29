from django.db import models

class Item(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity_left = models.IntegerField()
    item_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity_sold = models.IntegerField(default=0)
    item_stock_alert = models.IntegerField(default=1) 
    
    def __str__(self):
        return self.item_name




    
