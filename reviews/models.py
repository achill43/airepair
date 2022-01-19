from django.db import models


class Review(models.Model):
    image = models.ImageField(upload_to="img/reviews/", verbose_name="Изображение")
    sorting = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["sorting"]

try:
    from . import receivers
except ImportError:
    pass