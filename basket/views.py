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
        print(f'{product.name} last letter is {lastchar}')
        print(f'Add some product by id {product_id} to the basket')
        units = int(request.POST.get('units'))
        basket = request.session.get('basket', {})
        print(f'Basket: {basket}')

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
        print(request.session['basket'])
    except ValueError:
        messages.error(request, f'Write a correct number')

    return redirect(reverse('basket'))


def remove_from_basket(request, product_id):
    """
    A view to delete item from the shopping basket.

    For reasons I don't know the else statement is always executed
    Also the function doesn't remove the item from the basket. It
    only sets its value to 0 and then the template displays only
    items with value greater than 0.
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


def adjust_qty_on_stock(request, product_id):
    """
    View to Adjust products quantity on stock when the product
    is addded to the basket.

    Not in use at the moment.
    """

    print(f'Modify the product: {product_id} quantity on stock')
    basket = request.session.get('basket', {})
    units = int(request.POST.get('units'))
    product = get_object_or_404(Product, pk=product_id)
    print(f'Basket: {basket}')

    print(f'Modyfi the quantity of the product '
          f'from {product.quantity} to {units}')
    product.quantity = units

    request.session['basket'] = basket
    print(f'Print session {request.session["basket"]}')

    return redirect(reverse('basket'))
