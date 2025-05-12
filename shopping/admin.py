from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ShoppingList, Item

admin.site.register(ShoppingList)
admin.site.register(Item)
