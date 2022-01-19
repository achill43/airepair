import requests

from django import forms

from cart.models import Cart, Order, OrderItem


TOKEN = "5073599892:AAE_Du7efby87fdy3bVpB2PF6osDIITvlQ8"

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["full_name", "phone", "is_cleaning", "is_change_battery"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control js-phone-mask",
                "placeholder": "Введите телефон"
            }),
            "is_cleaning": forms.HiddenInput(),
            "is_change_battery": forms.HiddenInput()
        }

    def __init__(self, is_cleaning=None, is_change_battery=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if is_cleaning:
            self.initial["is_cleaning"] = True
        if is_change_battery:
            self.initial["is_change_battery"] = True

    def save(self, request):
        cd = self.cleaned_data.copy()
        session_key = request.session.session_key
        cart_obj = Cart.objects.get(session_key=session_key)
        order, created = Order.objects.get_or_create(
            cart=cart_obj,
            full_name=cd["full_name"],
            phone=cd["phone"],
            is_cleaning=cd["is_cleaning"]
        )
        created_item_list = []
        for cart_item in cart_obj.item.all():
            created_item_list.append(
                OrderItem(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )
            )
        if created_item_list:
            OrderItem.objects.bulk_create(created_item_list, ignore_conflicts=True)
        url = "https://api.telegram.org/bot"
        channel_id = 1686947971
        url += TOKEN
        method = url + "/sendMessage"
        text = f"У вас новый заказ: \n Имя: {order.full_name};\n Телефон: {order.phone};"
        text = str(text)
        if cd["is_cleaning"]:
            text = text + "\n На чистку наушников;"
        if cd["is_change_battery"]:
            text = text + "\n На замену АКБ;"
        for item in created_item_list:
            text = text + "\n" + item.product.title

        r = requests.post(
            method, data={
                "chat_id": channel_id,
                "text": text
            }
        )
        request.session.create()

        return order
