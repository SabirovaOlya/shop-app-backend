from django.urls import path
from apps.products.views import ProductListCreateAPIView, ProductDetailAPI

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<uuid:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
]
