from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def all_products(request):
    """
    A view to show all products.
    """

    products = Product.objects.all()
    # excluded_category = get_object_or_404(Category, name='services')

    # products = all_products.filter(excluded_category!=excluded_category)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
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
    category = get_object_or_404(Category, name='services')
    print(f"\nChoosen category: {category}")
    categories = Category.objects.all()
    products = Product.objects.all()
    services = products.filter(category=category)
    print(f'Products: {products}')
    print(f'Services: {services}')
    for serv in services:
        print(f'service name - {serv.name}')
    # if request.GET:
    #         services = products.filter(category=='services')
    # result = list(filter(lambda x: (x % 13 == 0), my_list)) 
    

    context = {
        'services': services,
    }
    return render(request, 'products/workshop.html', context)
    
    
@login_required
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


@login_required
def edit_product(request, product_id):
    """
    A view to edit an existing product by its id.
    """
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            print("Product updated")
            return redirect(reverse("products"))
        else: 
            print("\n\n\n Update didn't succeed")

    context = {
        'product_id': product_id,
        'form': form,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete an existing product by its id.
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect(reverse('products'))
 
 
def subtract_products(request, product_id, number):
    """
    A view to Update product quantity when the product is 
    added to the basket.
    """
    product = get_object_or_404(Product, pk=product_id)
    product.quantity -= number
