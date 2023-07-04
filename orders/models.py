from django.db import models

# model for received orders
class received_order(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_cost = models.IntegerField()
    item_quantity = models.IntegerField()




