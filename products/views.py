from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product


class ProductsListView(ListView):
    template_name = "catalog.html"
    queryset = Product.objects.all()
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product
    context_object_name = "product"
