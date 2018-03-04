from django.views import generic
from django.urls import reverse_lazy
from .models import Money


class IndexView(generic.ListView):
    model = Money
    paginate_by = 8
    ordering = ['-use_at']
    template_name = "moneyfly/index.html"


class DetailView(generic.DetailView):
    model = Money
    template_name = "moneyfly/detail.html"


class CreateView(generic.edit.CreateView):
    model = Money
    fields = "__all__"
    template_name = "moneyfly/create.html"


class UpdateView(generic.edit.UpdateView):
    model = Money
    fields = "__all__"
    template_name = "moneyfly/update.html"


class DeleteView(generic.edit.DeleteView):
    model = Money
    success_url = reverse_lazy("moneyfly:index")
    template_name = "moneyfly/delete.html"
