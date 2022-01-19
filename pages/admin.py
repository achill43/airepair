from django.contrib import admin

from .models import Service, YouToUs, GoodToKnow, YouGet, Galery, CleaningSlider


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "time", "sorting"]
    list_editable = ["sorting"]


@admin.register(YouToUs)
class YouToUsAdmin(admin.ModelAdmin):
    list_display = ["text", "sorting"]
    list_editable = ["sorting"]


@admin.register(GoodToKnow)
class GoodToKnowAdmin(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(YouGet)
class YouGetAdmin(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "sorting"]
    list_editable = ["sorting"]


@admin.register(CleaningSlider)
class CleaningSliderAdmin(admin.ModelAdmin):
    pass
