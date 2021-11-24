from django.contrib import admin
from . models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Customer)
admin.site.register(Product, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)