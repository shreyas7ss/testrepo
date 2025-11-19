from typing import Optional
from dataclasses import dataclass
from rest_framework import serializers

class Order:
    def __init__(self, id: int, customer: Optional[str], items: Optional[list] = None):
        self.id = id
        self.customer = customer
        self.items = items if items is not None else []

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer = serializers.CharField(allow_null=True)
    items = serializers.ListField(allow_null=True, required=False)

    def to_representation(self, instance: Order):
        data = super().to_representation(instance)
        if instance.items is None:
            data['items'] = []
        return data

    def to_internal_value(self, data: dict):
        if 'items' in data and data['items'] is None:
            data['items'] = []
        return super().to_internal_value(data)