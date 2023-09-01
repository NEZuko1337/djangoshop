from django.contrib import admin
from . models import Product, ProductCategory, Basket
admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)

# Удобная работа с админкой
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    readonly_fields = ['name', 'price']
    ordering = ['name']