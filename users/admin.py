from django.contrib import admin
from carts.admin import CartTabAdmin
from .models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email']
    list_editable = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']

    inlines = [CartTabAdmin, ]