from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('guarantee/new/', views.ProductNewView.as_view(), name='new'),
    path('guarantee/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('guarantee/<int:pk>/update', views.ProductUpdateView.as_view(), name='update'),
    path('guarantee/<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete'),
]