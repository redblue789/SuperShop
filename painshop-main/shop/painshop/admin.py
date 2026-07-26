from django.contrib import admin
from .models import Product, Category

# Реєструємо категорії та товари в адмінці
admin.site.register(Category)
admin.site.register(Product)