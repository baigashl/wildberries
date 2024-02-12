from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import(
    ProductListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductViewSet,
    ProductFilterListAPIView,
    CartAPIView,
    CartUpdateAPIView,
    CartResetAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),

    path('cart/<int:id>', CartAPIView.as_view(), name='cart'),
    path('cart/<int:id>/update/', CartUpdateAPIView.as_view(), name='cart-update'),
    path('cart/<int:id>/reset/', CartResetAPIView.as_view(), name='cart-reset'),

    path('filter/', ProductFilterListAPIView.as_view(), name='product-filter'),
]
