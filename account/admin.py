from django.contrib import admin
from . models import Products,Cart,Orders
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','stock')
admin.site.register(Products,ProductAdmin)
admin.site.register(Cart)
admin.site.register(Orders)

