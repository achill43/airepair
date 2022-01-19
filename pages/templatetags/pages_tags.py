import os

from django import template
from django.conf import settings

from pages.models import Service, YouToUs, GoodToKnow, YouGet, CleaningSlider
from pages.utils import ImageThumbnail

register = template.Library()


@register.simple_tag
def get_cleaning_slider():
    return CleaningSlider.objects.all()


@register.simple_tag
def get_services():
    return Service.objects.all()


@register.simple_tag
def get_you_to_us():
    return YouToUs.objects.all()


@register.simple_tag
def get_good_to_know():
    return GoodToKnow.objects.all()


@register.simple_tag
def get_you_get():
    return YouGet.objects.all()


@register.simple_tag()
def image_watermark(imgUrl):
    imgUrl = str(imgUrl)
    saveUrl = str(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_URL)+ os.path.basename(imgUrl))
    returnImg = str(settings.MEDIA_URL) + str(settings.THUMBNAIL_URL) + os.path.basename(imgUrl)
    text = "AIREPAIR"
    ImageThumbnail.add_watermart_text(imgUrl, saveUrl, text)
    return returnImg


@register.simple_tag
def static_image_watermark(filename):
    imgUrl = f"{settings.BASE_DIR}{settings.STATIC_URL}{filename}"
    saveUrl = str(os.path.join(settings.MEDIA_ROOT, settings.THUMBNAIL_URL) + os.path.basename(filename))
    returnImg = str(settings.MEDIA_URL) + str(settings.THUMBNAIL_URL) + os.path.basename(imgUrl)
    is_exit = os.path.exists(saveUrl)
    if not is_exit:
        text = "AIREPAIR"
        ImageThumbnail.add_watermart_text(imgUrl, saveUrl, text)
    return returnImg