from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.views import cart_detail  # функция для получения товаров из корзины
from main.models import Product

# пример order_create
def order_create(request):
    cart = request.session.get("cart", {})
    if not cart:
        return redirect("main:product_list")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product_id, quantity in cart.items():
                OrderItem.objects.create(
                    order=order,
                    product_id=product_id,
                    price=Product.objects.get(id=product_id).price,
                    quantity=quantity
                )
            request.session["cart"] = {}
            return render(request, "orders/order_created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orders/order_create.html", {"form": form})

