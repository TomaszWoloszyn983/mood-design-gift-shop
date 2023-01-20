from django.shortcuts import render

def show_basket(request):
    """
    A view to show products added to the shopping basket.
    """

    return render(request, 'basket/basket.html')
