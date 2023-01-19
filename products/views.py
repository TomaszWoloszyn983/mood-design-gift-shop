from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products.
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
    return render(request, 'products/product_detail.html', context)


def workshop(request):
    """
    A view to show the workshop template.

    If workshop services will be a separate category of products
    This function is going to return products of this category.
    """
    # products = Product.objects.all()

    # context = {
    #     'products': products,
    # }
    return render(request, 'products/workshop.html')
    

def add_product(request):
    """
    A view to add the new product to database.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Product added")
            return redirect(reverse("products"))
        else: 
            print("\n\n\n Adding the product didn't succeed")
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


def edit_product(request, product_id):
    """
    A view to edit an existing product by its id.
    """
    up_product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=up_product)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("Product updated")
            return redirect(reverse("products"))
        else: 
            print("\n\n\n Uodate didn't succeed")

    context = {
        'product_id': product_id,
        'form': form,
    }
    return render(request, 'products/edit_product.html', context)
 