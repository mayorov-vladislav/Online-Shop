from rest_framework import serializers
from .models import * 


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'created_timestamp', 'phone_number', 'requires_delivery', 'delivery_address', 'payment_on_get', 'is_paid', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'name', 'price', 'quantity', 'created_timestamp']