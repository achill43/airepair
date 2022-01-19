"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

from pages.views import GaleryListView
from products.views import ProductsListView, ProductDetailView
from reviews.views import ReviewListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("galery/", GaleryListView.as_view(), name="galery"),
    path("catalog/", ProductsListView.as_view(), name="catalog"),
    path(
        "catalog/product-detail/<int:pk>",
        ProductDetailView.as_view(),
        name="product_detail"
    ),
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path("delivery/", TemplateView.as_view(
        template_name='delivery.html',), name="delivery"),
    path("connect/", TemplateView.as_view(
        template_name='connect.html',), name="connect"),
    path("cleaning/", TemplateView.as_view(
        template_name='cleaning.html',), name="cleaning"),
    path("", TemplateView.as_view(
        template_name='homepage.html',), name="homepage"),
    path("cart/", include("cart.urls")),
]

urlpatterns.extend(static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
