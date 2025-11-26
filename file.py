from typing import Optional

class Order:
    def __init__(self, items: Optional[list] = None, customer: Optional[object] = None):
        self.items = items
        self.customer = customer

    def process_order(self) -> None:
        if self.items is not None:
            # process items
            for item in self.items:
                print(item)
        else:
            print("Order items are None")

        if self.customer is not None:
            # process customer
            print(self.customer)
        else:
            print("Order customer is None")
