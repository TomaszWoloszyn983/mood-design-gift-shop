from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect, reverse
from django.contrib import messages
from products.models import Product


def show_basket(request):
    """
    A view to show products added to the shopping basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """
    A view to add product to the shopping basket.
    """
    try:
        product = Product.objects.get(pk=product_id)
        lastchar = product.name[-1]
        units = int(request.POST.get('units'))
        basket = request.session.get('basket', {})

        if product_id in list(basket.keys()):
            basket[product_id] += units
        else:
            basket[product_id] = units
            if units == 1:
                messages.success(request, f'Added {units} {product.name} to '
                                          f'your shopping basket')
            elif lastchar == 'h':
                messages.success(request, f'Added {units} {product.name}es to '
                                          f'your shopping basket')
            else:
                messages.success(request, f'Added {units} {product.name}s to '
                                          f'your shopping basket')

        request.session['basket'] = basket
    except ValueError:
        messages.error(request, f'The quantity value was incorrect.'
                                f'\nPlease enter a numeric value')
    return redirect(reverse('basket'))


def remove_from_basket(request, product_id):
    """
    A view to delete item from the shopping basket.
    """

    product = get_object_or_404(Product, pk=product_id)
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket.pop(product_id)
        messages.success(request, f'Removed {product.name}s from your '
                                  f'shopping basket')
    else:
        messages.success(request, f'I could not remove {product.name}s '
                                  f'from the basket')

    request.session['basket'] = basket
    return redirect(reverse('basket'))
