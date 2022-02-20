from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    """
    Django 기본 뷰를 상속받은 Product list view.
    Get mothod로 메인 페이지에 매핑되어 있습니다.
    """

    model = Product
    context_object_name = "product_list"
    template_name = "product/list.html"


class ProductDetailView(DetailView):
    """
    Product detail view.
    Get method로 개별 객체의 Primary key가 Path parameter로 매핑되어 있습니다.
    """

    model = Product
    context_object_name = "product"
    template_name = "product/detail.html"


class ProductNewView(CreateView):
    """
    Product create view.
    Creation 후 리디렉션 경로만 Customizing.
    """

    model = Product
    form_class = ProductForm
    template_name = "product/edit.html"

    def get_success_url(self):
        return reverse_lazy("products:list", kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    """
    Product update view.
    """

    model = Product
    form_class = ProductForm
    template_name = "product/edit.html"

    def get_success_url(self):
        return reverse_lazy("products:detail", kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    """
    Product delete view.
    정상 삭제 시 메인페이지로 리디렉션.
    """

    model = Product
    context_object_name = "product"
    template_name = "product/delete.html"
    success_url = "/"
