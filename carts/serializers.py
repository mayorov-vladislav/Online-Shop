from rest_framework import serializers
from .models import * 

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity', 'created_timestamp']
        