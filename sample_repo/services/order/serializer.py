from typing import Optional
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance: Optional[Order]) -> dict:
        # Check for None to prevent null pointer exceptions
        if instance is None:
            raise serializers.ValidationError('Order instance is None')
        # Call the parent method to perform the serialization
        return super().to_representation(instance)
