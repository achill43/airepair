from django.contrib import admin

from products.models import Product, ProductImage


class ProductImageTabularInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "model", "price", "sorting"]
    list_editable = ["sorting"]
    inlines = [
        ProductImageTabularInline,
    ]
