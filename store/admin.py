from django.contrib import admin
from .models import Product, Colors, Sizes

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'price', 'stock', 'category', 'updated_at', 'is_available',)
	prepopulated_fields = {'slug':('product_name',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Colors)
admin.site.register(Sizes)
 