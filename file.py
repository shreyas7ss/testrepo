class OrderSerializer:
    def serialize(self, order: dict) -> dict:
        if order is None:
            return None
        try:
            if 'items' in order and order['items'] is not None:
                return {'status': 'ok', 'data': {'order_id': order.get('id'), 'items': order['items']}}
            else:
                return {'status': 'ok', 'data': {'order_id': order.get('id'), 'items': []}}
        except Exception as e:
            raise ValueError(f'Serialization failed: {e}')