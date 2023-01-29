from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe

# Create your views here.
def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'The basket is empty')
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Set your Stripe public key in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MFBRILWWeH2Y5WlTvWhOsM4yRoTrAo6FaQQeTuypLAJe8B0tZUKOyFVLIHmb1xFl3V2jqOo4FLCJnr9zOqSfZKb00PrYaYpUv',
        'client_secret': 'intent.client secret',
    }

    return render(request, template, context)
