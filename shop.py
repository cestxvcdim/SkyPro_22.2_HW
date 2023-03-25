from exceptions import NotEnoughCapacity, NotEnoughTypes
from storage import Store


class Shop(Store):
    def __init__(self, items: dict, capacity: int) -> None:
        """Construct"""
        super().__init__(items, capacity)

    def add(self, quantity, title):
        """Add a commodities but items in shop should be less than 5"""
        if self.get_unique_items_count() == 5:
            raise NotEnoughTypes
        if quantity < self.capacity:
            self.capacity -= quantity
            self.items[title] = quantity
        else:
            raise NotEnoughCapacity
