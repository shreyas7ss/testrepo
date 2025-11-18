from typing import Optional

from pydantic import BaseModel

class Order(BaseModel):
    id: int
    customer_id: int
    order_date: str

    class Config:
        orm_mode = True

def serialize_order(order: Optional[Order]) -> dict:
    # Check if order is None to prevent null pointer exception
    if order is None:
        # Handle the case when order is None, for example, return an empty dictionary
        return {}
    
    # If order is not None, proceed with serialization
    return order.dict()