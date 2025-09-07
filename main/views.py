from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# # список товаров
# def product_list(request):
#     products = Product.objects.filter(available=True)  # только доступные
#     return render(request, "main/product_list.html", {"products": products})

# # страница товара
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, available=True)
#     return render(request, "main/product_detail.html", {"product": product})

def product_list(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'main/product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'main/product_detail.html', {'product': product})


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
