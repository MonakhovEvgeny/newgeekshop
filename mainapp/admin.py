from django.contrib import admin
from mainapp.models import Product, ProductCategory

# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantiti', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantiti'), 'category',)
    readonly_fields = ('description',)
    ordering = ('name', 'price')
    search_fields = ('name',)
