from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.Serializer):
    # Define the fields of the serializer
    id: int = serializers.IntegerField(read_only=True)
    customer_name: str = serializers.CharField(max_length=255)
    order_date: str = serializers.DateField()

    # Override the create method to add error handling
    def create(self, validated_data: dict) -> Order:
        # Check if the validated data is not None
        if validated_data is None:
            raise serializers.ValidationError("Validated data cannot be None")

        # Try to create a new order instance
        try:
            order = Order(**validated_data)
            order.save()
            return order
        except Exception as e:
            # Log the exception and raise a validation error
            print(f"Error creating order: {str(e)}")
            raise serializers.ValidationError("Failed to create order")