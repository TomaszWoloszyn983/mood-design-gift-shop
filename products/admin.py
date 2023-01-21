from django.contrib import admin
from.models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_on',
        'category',
        'price',
        'quantity',
        'image',
    )

    ordering = ('created_on',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Category)
