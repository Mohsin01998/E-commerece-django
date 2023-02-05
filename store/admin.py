from django.contrib import admin
from .models import OrderItem,Order,Product,Customer,ShippingAddress
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)

