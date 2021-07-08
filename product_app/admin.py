from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'price']

admin.site.register(Product,ProductAdmin)