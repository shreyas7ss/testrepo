'''Improved module with error handling.'''

class Serializer:
    def serialize(self, data):
        if data is None:
            return None
        try:
            return {"status": "ok", "data": data}
        except Exception as e:
            raise ValueError(f"Serialization failed: {e}")
