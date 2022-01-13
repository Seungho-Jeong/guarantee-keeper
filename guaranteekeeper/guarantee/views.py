from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Guarantee
from .forms import GuaranteeForm


class GuaranteeListView(ListView):
    """
    Django 기본 뷰를 상속받은 Guarantee list view.
    Get mothod로 메인 페이지에 매핑되어 있습니다.
    """

    model = Guarantee
    context_object_name = "guarantee_list"
    template_name = "guarantee/list.html"


class GuaranteeDetailView(DetailView):
    """
    Guarantee detail view.
    Get method로 개별 객체의 Primary key가 Path parameter로 매핑되어 있습니다.
    """

    model = Guarantee,
    context_object_name = "guarantee"
    template_name = "guarantee/detail.html"


class GuaranteeNewView(CreateView):
    """
    Guarantee create view.
    Creation 후 리디렉션 경로만 Customizing.
    """

    model = Guarantee
    form_class = GuaranteeForm
    template_name = "guarantee/edit.html"

    def get_success_url(self):
        return reverse_lazy("guarantee:detail", kwargs={'pk': self.object.pk})


class GuaranteeUpdateView(UpdateView):
    """
    Guarantee update view.
    """

    model = Guarantee
    form_class = GuaranteeForm
    template_name = "guarantee/edit.html"

    def get_success_url(self):
        return reverse_lazy("guarantee:detail", kwargs={'pk': self.object.pk})


class GuaranteeDeleteView(DeleteView):
    """
    Guarantee delete view.
    정상 삭제 시 메인페이지로 리디렉션.
    """

    model = Guarantee
    context_object_name = "guarantee"
    template_name = "guarantee/delete.html"
    success_url = "/"
