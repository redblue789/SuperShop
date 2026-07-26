from django.shortcuts import render


def index(request):
    products = [
        {
            'name': 'Pearl Necklace',
            'price': '$120',
            'category': 'necklace',
            'description': 'Елегантне перлове кольє для преміального образу.',
            'image': 'https://images.unsplash.com/photo-1617038220319-276d3cfab638?q=80&w=900&auto=format&fit=crop'
        },
        {
            'name': 'Gold Ring',
            'price': '$200',
            'category': 'ring',
            'description': 'Вишукана золота каблучка з сучасним дизайном.',
            'image': 'https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=900&auto=format&fit=crop'
        },
        {
            'name': 'Luxury Earrings',
            'price': '$90',
            'category': 'earrings',
            'description': 'Стильні сережки для вечірнього та повсякденного стилю.',
            'image': 'https://images.unsplash.com/photo-1535632787350-4e68ef0ac584?q=80&w=900&auto=format&fit=crop'
        },
    ]

    return render(request, 'shop/index.html', {'products': products})
