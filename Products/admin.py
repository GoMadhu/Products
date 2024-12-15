from django.contrib import admin

from .models import Products_List

class product_admin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_status','product_datestamp']

admin.site.register(Products_List, product_admin)

