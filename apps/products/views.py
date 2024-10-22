from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from apps.products.pagination import CustomPageNumberPagination


@extend_schema(tags=['products'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['products'])
class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
