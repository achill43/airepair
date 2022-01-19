from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart, Item
from cart.forms import OrderForm
from products.models import Product


def render_cart_template(request, context):
    html = render_to_string("cart/cart.html", context=context, request=request)
    return JsonResponse({
        "html": html,
        "quantity": context["cart_obj"].item.all().count()
    })


class CartView(View):
    template_name = "cart/cart.html"

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity", 1)
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        cart_obj, create = Cart.objects.get_or_create(session_key=session_key)
        if product_id:
            product_obj = Product.objects.filter(id=product_id).first()
            if product_obj:
                item_obj, create = Item.objects.get_or_create(cart=cart_obj, product=product_obj)
                item_obj.quantity = item_obj.quantity + quantity
                item_obj.save()
        context = {
            "request": request,
            "cart_obj": cart_obj,
            "order_form": OrderForm()
        }
        return render_cart_template(request, context)

    def get(self, request, *args, **kwargs):
        is_cleaning = request.GET.get("is_cleaning", None)
        is_change_battery = request.GET.get("is_change_battery", None)
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        cart_obj, create = Cart.objects.get_or_create(session_key=session_key)
        context = {
            "request": request,
            "cart_obj": cart_obj,
            "order_form": OrderForm(is_cleaning, is_change_battery),
            "is_cleaning": is_cleaning,
            "is_change_battery": is_change_battery
        }
        return render_cart_template(request, context)


def delete_item_from_cart(request, **kwargs):
    item_id = request.POST.get("item_id")
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key
    cart_obj, create = Cart.objects.get_or_create(session_key=session_key)
    item_obj = Item.objects.filter(id=item_id).first()
    if item_obj:
        item_obj.delete()
        context = {
            "request": request,
            "cart_obj": cart_obj,
            "order_form": OrderForm()
        }
    return render_cart_template(request, context)


class OrderFormView(FormView):
    template_name = "cart/cart.html"
    form_class = OrderForm

    def form_valid(self, form: OrderForm) -> JsonResponse:
        order = form.save(self.request)
        html = render_to_string("cart/order_form_success.html", context={
            "order": order,
        })
        return JsonResponse({
            "html": html
        })

    def form_invalid(self, form: OrderForm) -> JsonResponse:
        if not self.request.session.session_key:
            self.request.session.save()
        session_key = self.request.session.session_key
        cart_obj, create = Cart.objects.get_or_create(session_key=session_key)
        context = {
            "request": self.request,
            "cart_obj": cart_obj,
            "order_form": form
        }
        html = render_to_string(self.template_name, context=context, request=self.request)
        return JsonResponse({
            "html": html
        })
