from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

from django.contrib.admin.sites import AlreadyRegistered

try:
    admin.site.register(Product)
except AlreadyRegistered:
    pass