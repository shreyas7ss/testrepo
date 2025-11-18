class OrderSerializer:
    def serialize_order(self, order: object) -> dict:
        # Check if the order object is None to prevent null pointer exceptions
        if order is None:
            # Return None or raise an exception as per the requirement
            return None
        
        try:
            # Attempt to serialize the order object
            serialized_order = {
                'id': order.id,
                'customer_name': order.customer_name,
                'order_date': order.order_date
            }
            # Return the serialized order object
            return serialized_order
        except AttributeError as e:
            # Handle attribute errors that may occur during serialization
            print(f"Error serializing order: {e}")
            return None