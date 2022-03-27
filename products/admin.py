import imp
from django.contrib import admin
from products.models import Product,Offer

# Register your models here.
admin.site.register(Product)
admin.site.register(Offer)