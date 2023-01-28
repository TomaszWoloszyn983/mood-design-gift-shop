from django.shortcuts import render
from django.contrib import messages
from django.contrib import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe

# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'The basket is empty')
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MFBRILWWeH2Y5WlTvWhOsM4yRoTrAo6FaQQeTuypLAJe8B0tZUKOyFVLIHmb1xFl3V2jqOo4FLCJnr9zOqSfZKb00PrYaYpUv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
