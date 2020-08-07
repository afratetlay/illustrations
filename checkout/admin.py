from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number','grand_total',)

    fields = ('order_number', 'full_name', 'email', 
    'order_total', 'grand_total',)

    list_display = ('order_number', 'full_name', 'order_total', 'grand_total',)

    ordering = ('full_name',)

admin.site.register(Order, OrderAdmin)