from django import template


register = template.Library()


@register.filter(name='multiply')
def multiply(price, qty):
    return price * qty
