from django.contrib import admin
from apps.products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'count', 'created_at')
    list_filter = ('price', 'count', 'created_at')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]

    exclude = ('slug',)


@admin.register(ProductImage)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)
