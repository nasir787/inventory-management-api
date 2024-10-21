from django.urls import path
from .views import ItemCreateView, ItemDetailView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
