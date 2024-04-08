from rest_framework import serializers
from .models import * 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'slug', 'description', 'image', 'price', 'discount', 'quantity', 'category', 'total_price']