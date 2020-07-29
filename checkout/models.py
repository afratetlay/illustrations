import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


   """ Model to store order information, customer, 
    date ordered and if the order has been paid yet,
    I have not included address as the product will be sent 
    to the customer via email. """

class Order(models.Model):

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class OrderLineItem(models.Model):
    
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    