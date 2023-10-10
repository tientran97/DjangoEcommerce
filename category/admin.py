from django.contrib import admin
from .models import Category
from django.utils.html import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'preview_image' )
    ordering = ('-category_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def preview_image(self, obj):
        if obj.category_img:
            return mark_safe(f'<img src="{obj.category_img.url}" width="100" height="100" />')
        else:
            return 'No Image'

    preview_image.short_description = 'Image Preview'  # Column header text
admin.site.register(Category,CategoryAdmin)
