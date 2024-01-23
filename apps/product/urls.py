from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, CategoryCreateAPIView

urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
]