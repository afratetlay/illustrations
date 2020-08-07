import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product 

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum'] or 0
        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

   

class OrderLineItem(models.Model):
    
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems', default='0')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
         """
        Override the original save method to set the lineitem total
        and update the order total.
        """


    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
