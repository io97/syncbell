from django.views import generic
from .models import Money


class IndexView(generic.ListView):
    model = Money
    template_name = "money/index.html"
