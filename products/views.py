from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """
    A view to show all prosucts.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual prosuct details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'product/product_detail.html', context)