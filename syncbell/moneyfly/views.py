from django.views import generic
from django.urls import reverse_lazy
from .models import Money
from django.db.models import Sum

from datetime import date


class IndexView(generic.ListView):
    model = Money
    paginate_by = 5
    ordering = ['-use_at']
    template_name = "moneyfly/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 当月の合計金額
        this_y = date.today().year
        this_m = date.today().month
        context["month"] = this_m
        context["sum"] = Money.objects\
                         .filter(use_at__year = this_y,
                                 use_at__month = this_m)\
                         .aggregate(Sum('money'))["money__sum"]
        return context


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
