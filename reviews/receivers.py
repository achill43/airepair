from django.db.models.signals import post_save
from django.dispatch import receiver

from reviews.models import Review
from pages.utils import ImageThumbnail


@receiver(post_save, sender=Review)
def review_image_add_watermark(sender, instance, *args, **kwargs):
    imgUrl = str(instance.image.path)
    text = "AIREPAIR"
    ImageThumbnail.add_watermart_text(imgUrl, imgUrl, text)



