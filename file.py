from typing import Optional
from dataclasses import dataclass
from rest_framework import serializers

class Order:
    def __init__(self, id: int, customer: Optional[str], order_date: Optional[str]):
        self.id = id
        self.customer = customer
        self.order_date = order_date

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer = serializers.CharField(allow_null=True)
    order_date = serializers.CharField(allow_null=True)

    def to_representation(self, instance: Order):
        data = super().to_representation(instance)
        if instance.customer is None:
            data['customer'] = ''
        if instance.order_date is None:
            data['order_date'] = ''
        return data