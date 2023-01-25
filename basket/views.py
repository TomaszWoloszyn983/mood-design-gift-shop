from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product

def show_basket(request):
    """
    A view to show products added to the shopping basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """
    A view to add product to the shopping basket.

    It's planned to add product quantity variable to the product model
    This value would be updated in this function.
    Also it has to check if the product quantity is not already 0 
    to be able to add the product to the basket.
    """

    print(f'Add some product by id {product_id} to the basket')
    units = int(request.POST.get('units'))
    basket = request.session.get('basket', {})
    print(f'Basket: {basket}')

    if product_id in list(basket.keys()):
        basket[product_id] += units
    else:
        basket[product_id] = units

    request.session['basket'] = basket
    print(request.session['basket'])

    return redirect(reverse('basket'))


def remove_from_basket(request, product_id):
    """
    A view to delete item from the shopping basket.

    For reasons I don't know the else statement is always executed
    Also the function doesn't remove the item from the basket. It 
    only sets its value to 0 and then the template displays only 
    items with value greater than 0.
    """

    print(f'Remove product with id: {product_id} from the basket')
    basket = request.session.get('basket', {})
    print(f'Basket: {basket}')

    if product_id in list(basket.keys()):
        basket[product_id] = 0
        print('\n\n\nOption 1')
    else:
        basket[product_id] = 0
        print('\n\n\nOption 2')

    request.session['basket'] = basket
    print(f'Print session {request.session["basket"]}')

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

    print(f'Modyfi the quantity of the product from {product.quantity} to {units}')
    product.quantity = units

    request.session['basket'] = basket
    print(f'Print session {request.session["basket"]}')

    return redirect(reverse('basket'))
