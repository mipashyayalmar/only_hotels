from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate, Advertise
from .models import Table

admin.site.register(Table)

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'subcategory', 'price', 'pub_date')
    search_fields = ('product_name', 'category', 'subcategory')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timestamp')
    search_fields = ('name', 'email', 'phone')

class OrdersAdmin(admin.ModelAdmin):
    # Since name, email, city, state, and zip_code are removed, display only the relevant fields
    list_display = ('order_id', 'userId', 'amount', 'address', 'phone', 'timestamp')
    search_fields = ('order_id', 'userId', 'phone')

class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'update_desc', 'timestamp')
    search_fields = ('order_id', 'update_desc')

class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering the models with the custom admin configurations
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderUpdate, OrderUpdateAdmin)
admin.site.register(Advertise, AdvertiseAdmin)
