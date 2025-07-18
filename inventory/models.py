from django.db import models

# Create your models here.
from django.db import models

class Product( models.Model):
    name = models.CharField(max_length=100, unique = True, help_text="product name")
    description = models.TextField(blank = True, null = True, help_text="product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="price of product")
    quantity = models.IntegerField(default=0, help_text="quantity in stock currently")
    low_stock_threshold = models.IntegerField(db_default=10, help_text="for low stock alert")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    