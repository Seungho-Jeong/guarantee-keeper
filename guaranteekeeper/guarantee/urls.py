from django.urls import path

from . import views

app_name = "guarantee"

urlpatterns = [
    path('', views.GuaranteeListView.as_view(), name='list'),
    path('guarantee/<int:pk>/', views.GuaranteeDetailView.as_view(), name='detail'),
    path('guarantee/new/', views.GuaranteeNewView.as_view(), name='new'),
    path('guarantee/<int:pk>/update/', views.GuaranteeUpdateView.as_view(), name='update'),
    path('guarantee/<int:pk>/delete/', views.GuaranteeDeleteView.as_view(), name='delete'),
]
