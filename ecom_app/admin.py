from django.contrib import admin

from .models import Contact, Product

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display= ['name', 'email', 'phone_numb']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display= ['product_name', 'category', 'subcategory', 'price']