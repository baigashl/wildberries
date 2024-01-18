from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
]