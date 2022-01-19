from django.urls import path

from cart.views import CartView, delete_item_from_cart, OrderFormView

urlpatterns = [
    path("add/", CartView.as_view(), name="add_to_cart"),
    path("delete/", delete_item_from_cart, name="delete_from_cart"),
    path("order-form/", OrderFormView.as_view(), name="order_form")
]
