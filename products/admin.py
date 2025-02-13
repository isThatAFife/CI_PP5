from django.contrib import admin
from .models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
