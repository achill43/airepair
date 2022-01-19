from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    sub_title = models.CharField(max_length=100, verbose_name="Текст")
    model = models.CharField(max_length=100, verbose_name="Модель")
    price = models.PositiveIntegerField()
    sorting = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["sorting"]

    def __str__(self) -> str:
        return f"{self.title} - {self.price}"

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})

    def get_first_img(self):
        return self.images.first().img


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images",
        verbose_name="Продукт"
    )
    img = models.FileField(upload_to="img/products/")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"