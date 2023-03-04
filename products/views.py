from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def all_products(request):
    """
    A view to show all products except of the products marked
    with services category.
    Services are displayed in the workshop section.
    """

    excluded_category = get_object_or_404(Category, name='services')
    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'excluded_category': excluded_category,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def workshop(request):
    """
    A view to show the workshop template.

    This functions returns only products market with services category.
    """
    category = get_object_or_404(Category, name='services')
    products = Product.objects.all().order_by('-created_on')

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'products/workshop.html', context)


@login_required
def add_product(request):
    """
    A view to add the new product to database.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            price = float(request.POST.get("price"))
            quantity = int(request.POST.get("quantity"))
            if price < 0 or quantity < 0:
                raise ValueError('Negative Value Error!')
            if form.is_valid():
                form.save()
                messages.success(request, f'Item successfully added.')
                return redirect(reverse("products"))
            else:
                messages.error(request, f'A problem occured! '
                               f'I could not update this item')
        except ValueError as e:
            messages.error(request, f'Some of your input boxes '
                           'contain negative values. '
                           'Please enter a positive value.')
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        price = float(request.POST.get("price"))
        quantity = int(request.POST.get("quantity"))
        try:
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                if price < 0 or quantity < 0:
                    raise ValueError('Negative value error')
                form.save()
                messages.success(request, f'Item {product.name} '
                                 f'successfully updated')
                return redirect(reverse("products"))
            else:
                messages.error(request, f'A problem occured! '
                               f'I could not update this item')
        except ValueError as e:
            messages.error(request, f'Some of your input boxes '
                           'contain negative values. '
                           'Please enter a positive value.')

    context = {
        'product_id': product_id,
        'form': form,
        'is_workshop': False,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete an existing product by its id.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Item {product.name} successfully deleted')

    return redirect(reverse('products'))


@login_required
def edit_service(request, product_id):
    """
    A view to edit an existing workshop product by its id.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        price = float(request.POST.get("price"))
        quantity = int(request.POST.get("quantity"))
        form = ProductForm(request.POST, request.FILES, instance=product)
        try:
            if form.is_valid():
                if price < 0 or quantity < 0:
                    raise ValueError('Negative value error')
                form.save()
                messages.success(request, f'Item workshop {product.name} '
                                 f'successfully updated .')
                return redirect(reverse("workshop"))
            else:
                messages.error(request, f"Service update didn't succeed")
        except ValueError as e:
            messages.error(request, f'Some of your input boxes '
                           'contain negative values. '
                           'Please enter a positive value.')

    context = {
        'product_id': product_id,
        'form': form,
        'is_workshop': True,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_service(request, product_id):
    """
    A view to delete an existing workshop product by its id.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Item {product.name} successfully deleted')

    return redirect(reverse('workshop'))
