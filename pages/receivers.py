from django.db.models.signals import post_save
from django.dispatch import receiver

from pages.models import Galery, CleaningSlider
from pages.utils import ImageThumbnail


@receiver(post_save, sender=Galery)
def galery_image_add_watermark(sender, instance, *args, **kwargs):
    imgUrl = str(instance.image.path)
    text = "AIREPAIR"
    ImageThumbnail.add_watermart_text(imgUrl, imgUrl, text)


@receiver(post_save, sender=CleaningSlider)
def cleaning_slider_image_add_watermark(sender, instance, *args, **kwargs):
    imgUrl = str(instance.img.path)
    text = "AIREPAIR"
    ImageThumbnail.add_watermart_text(imgUrl, imgUrl, text)
