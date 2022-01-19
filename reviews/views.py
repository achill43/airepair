from django.views.generic import ListView

from reviews.models import Review


class ReviewListView(ListView):
    template_name = "reviews.html"
    queryset = Review.objects.all()
    context_object_name = "reviews"
