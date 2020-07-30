from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product 

class Order(models.Model):

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return {self.name}

def update_total(self):
    self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum']


class OrderLineItem(models.Model):
    
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return {self.product} 
