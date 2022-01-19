from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Cart(models.Model):
    session_key = models.CharField(_("Сесия"), max_length=100)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Корзина"), related_name="item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Товар"), related_name="cart_item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Количество"), default=0)

    class Meta:
        verbose_name = _("Продукт корзины")
        verbose_name_plural = _("Предметы")

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity}"

    def total_price(self) -> int:
        return self.product.price * self.quantity


class Order(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.SET_NULL, verbose_name="Корзина", related_name="order", null=True, blank=True)
    full_name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=25, verbose_name="Телефон")
    is_cleaning = models.BooleanField(default=False, verbose_name="Чистка наушников")
    is_change_battery = models.BooleanField(default=False, verbose_name="Замена АКБ")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"

    def order_number(self):
        return self.id + 1000


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, verbose_name=_("Товар"), related_name="order_item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Количество"), default=0)

    class Meta:
        verbose_name = "Продукт Заказа"

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"

    def total_price(self) -> int:
        return self.product.price * self.quantity
