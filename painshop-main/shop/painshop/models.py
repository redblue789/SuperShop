from django.db import models

# НОВА МОДЕЛЬ ДЛЯ КАТЕГОРІЙ
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ОНОВЛЕНА МОДЕЛЬ ТОВАРУ
class Product(models.Model):
    # Зв'язок із категорією
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='paint_images/', null=True, blank=True)

    def __str__(self):
        return self.name