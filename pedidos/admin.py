from django.contrib import admin
from .models import Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'is_paid', 'total_price', 'created_at')
    list_filter = ('status', 'is_paid', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Product)