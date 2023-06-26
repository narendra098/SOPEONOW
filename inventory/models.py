from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    quantity_sold = models.IntegerField(default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name




    
