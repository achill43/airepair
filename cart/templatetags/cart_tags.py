from django import template

from cart.models import Cart

register = template.Library()

@register.inclusion_tag(
    'cart/mini_cart.html',
    takes_context=True, name='mini_cart'
)
def mini_cart(context):
    request = context['request']
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key
    cart_obj, create = Cart.objects.get_or_create(session_key=session_key)
    return {
        'cart': cart_obj,
        "quantity": cart_obj.item.all().count(),
        'request': request
    }
