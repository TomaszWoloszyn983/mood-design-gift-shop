from django.shortcuts import render, get_object_or_404, redirect, reverse

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
    basket = request.session.get('basket', {})

    basket[product_id] = True

    return redirect(reverse('basket'))

    # product = 

# def delete_product(request, product_id):
#     """
#     A view to delete an existing product by its id.
#     """
#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()


#     return redirect(reverse('products'))
