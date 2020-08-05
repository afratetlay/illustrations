from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('grand_total',)

    fields = ('full_name', 'email', 
    'order_total', 'grand_total',)

    list_display = ('full_name', 'order_total', 'grand_total',)

admin.site.register(Order, OrderAdmin)