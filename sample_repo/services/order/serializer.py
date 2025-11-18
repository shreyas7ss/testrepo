from typing import Optional

class OrderSerializer:
    def __init__(self, order: Optional[dict]) -> None:
        # Check if order is None to prevent null pointer exception
        if order is None:
            raise ValueError("Order cannot be None")
        self.order = order

    def serialize(self) -> dict:
        # Check if order is not None before attempting to serialize
        if self.order is not None:
            # Assuming order has 'id' and 'customer' keys
            return {
                'id': self.order.get('id'),
                'customer': self.order.get('customer')
            }
        else:
            # Handle the case where order is None
            return {}