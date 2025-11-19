from typing import Optional, List

class Order:
    def __init__(self, id: int, items: Optional[List[str]] = None):
        self.id = id
        self.items = items if items is not None else []


class OrderSerializer:
    def serialize(self, order: Order) -> dict:
        try:
            return {
                'id': order.id,
                'items': order.items
            }
        except Exception as e:
            # Log or handle the exception as needed
            print(f'Error serializing order: {str(e)}')
            return {}