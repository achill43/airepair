from django.contrib import admin
from django.db import models

from cart.models import Cart, Item, Order

class ItemTabularInline(admin.TabularInline):
    model = Item
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ItemTabularInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone", "is_cleaning"]
