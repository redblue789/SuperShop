from django.shortcuts import render, redirect
from .models import Product, Category

def product_list(request):
    # Беремо всі категорії з бази даних
    categories = Category.objects.all()
    
    # Логіка кошика залишається без змін
    cart_ids = request.session.get('cart', [])
    cart_items = Product.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)
    
    return render(request, 'shop/product_list.html', {
        'categories': categories, # Тепер передаємо категорії
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': len(cart_ids)
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('product_list')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
    return redirect('product_list')