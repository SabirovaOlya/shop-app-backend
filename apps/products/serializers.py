from rest_framework import serializers
from apps.products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'count', 'discount', 'description', 'created_at', 'updated_at',
                  'images']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        product = Product.objects.create(**validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)

        return product
