from django.urls import path
from . import views

app_name = "moneyfly"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("money/create/", views.CreateView.as_view(), name="create"),
    path("money/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("money/<int:pk>/update/", views.UpdateView.as_view(), name="update"),
    path("money/<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]
