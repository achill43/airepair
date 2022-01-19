from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    time = models.PositiveIntegerField(verbose_name="Время ремонта")
    icon = models.CharField(max_length=50, verbose_name="Иконка")
    sorting = models.PositiveIntegerField(default=0)
    link = models.URLField(max_length=100, verbose_name="Ссылка", blank=True, null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["sorting"]


class YouToUs(models.Model):
    text = models.CharField(max_length=255, verbose_name="Текст")
    sorting = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Тебе к нам если"
        verbose_name_plural = "Тебе к нам если"
        ordering = ["sorting"]


class GoodToKnow(models.Model):
    text = models.TextField()
    sorting = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Полезно знать"
        verbose_name_plural = "Полезно знать"
        ordering = ["sorting"]


class YouGet(models.Model):
    text = models.TextField()
    sorting = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ты получишь"
        verbose_name_plural = "Ты получишь"
        ordering = ["sorting"]


class CleaningSlider(models.Model):
    img = models.FileField(upload_to="img/cleaning/", verbose_name="Изображение")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class Galery(models.Model):
    image = models.FileField(upload_to="img/galery/", verbose_name="Изображение")
    alt_text = models.CharField(max_length=255, verbose_name="Alt текст")
    is_gif = models.BooleanField(default=False, verbose_name="Если GIF")
    sorting = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        ordering = ["sorting"]

try:
    from . import receivers
except ImportError:
    pass