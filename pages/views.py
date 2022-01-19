from django.views.generic import ListView

from pages.models import Galery


class GaleryListView(ListView):
    template_name = "galery.html"
    queryset = Galery.objects.all()
    context_object_name = "galeries"
