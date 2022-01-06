from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Guarantee
from .forms import GuaranteeForm


class GuaranteeListView(ListView):
    model = Guarantee
    context_object_name = "guarantee_list"
    template_name = "guarantee/list.html"


class GuaranteeDetailView(DetailView):
    model = Guarantee
    context_object_name = "guarantee"
    template_name = "guarantee/detail.html"


class GuaranteeNewView(CreateView):
    model = Guarantee
    form_class = GuaranteeForm
    template_name = "guarantee/edit.html"

    def get_success_url(self):
        return reverse_lazy("guarantee:detail", kwargs={'pk': self.object.pk})


class GuaranteeUpdateView(UpdateView):
    model = Guarantee
    form_class = GuaranteeForm
    template_name = "guarantee/edit.html"

    def get_success_url(self):
        return reverse_lazy("guarantee:detail", kwargs={'pk': self.object.pk})


class GuaranteeDeleteView(DeleteView):
    model = Guarantee
    context_object_name = "guarantee"
    template_name = "guarantee/delete.html"
    success_url = "/"
