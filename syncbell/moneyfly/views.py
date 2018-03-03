from django.views import generic
from django.urls import reverse_lazy
from .models import Money


class IndexView(generic.ListView):
    model = Money
    template_name = "money/index.html"


class DetailView(generic.DetailView):
    model = Money
    template_name = "money/detail.html"


class CreateView(generic.edit.CreateView):
    model = Money
    fields = "__all__"
    template_name = "money/update.html"


class UpdateView(generic.edit.UpdateView):
    model = Money
    fields = "__all__"
    template_name = "money/update.html"


class DeleteView(generic.edit.DeleteView):
    model = Money
    success_url = reverse_lazy("moneyfly:index")
    template_name = "money/delete.html"
