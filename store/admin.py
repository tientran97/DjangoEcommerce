from django.contrib import admin
from .models import Product
from django.utils.html import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','preview_image', 'category', 'price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


    def preview_image(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="100" height="100" />')
        else:
            return 'No Image'

    preview_image.short_description = 'Image Preview'  # Column header text
admin.site.register(Product, ProductAdmin)
