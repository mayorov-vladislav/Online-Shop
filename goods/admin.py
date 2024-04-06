from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['id', 'name']
    list_editable = ['name', ]
    search_fields = ['id', 'name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['id', 'name', 'quantity', 'price', 'discount', 'category']
    list_editable = ['name', 'quantity', 'price', 'discount', 'category']
    search_fields = ['id', 'name', 'quantity', 'price', 'category']
    list_filter = ['price', 'discount', 'quantity', 'category']
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
