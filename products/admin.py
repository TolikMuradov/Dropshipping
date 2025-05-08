from django.contrib import admin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name', 'price_local', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

    def preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="60" />')
        return "-"