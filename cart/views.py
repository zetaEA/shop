from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product

# Показать корзину
def cart_detail(request):
    cart = request.session.get("cart", {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)
    return render(request, "cart/cart_detail.html", {"products": products, "total": total})

# Добавить товар
def cart_add(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("cart:cart_detail")

def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    pid = str(product_id)
    if pid in cart:
        if cart[pid] > 1:
            cart[pid] -= 1
        else:
            del cart[pid]
    request.session["cart"] = cart
    return redirect("cart:cart_detail")
