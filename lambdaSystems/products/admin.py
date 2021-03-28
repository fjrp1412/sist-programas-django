from django.contrib import admin

# Register your models here.
from products.models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id_product', 'name', 'category', 'brand', 'price', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)