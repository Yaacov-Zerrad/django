from django.contrib import admin
from .models import Products

# Register your models here.

# enregistre table
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'activate', 'slug')
    
    
admin.site.register(Products, AdminProduct)