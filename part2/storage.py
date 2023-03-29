from abc import ABC, abstractmethod

from part2.exceptions import NotEnoughCapacity


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict, capacity: int):
        self.items: dict = items
        self.capacity: int = capacity

    @abstractmethod
    def add(self, title: str, quantity: int):
        """Add anything to anywhere (storage)"""
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int):
        """Remove anything from anywhere (storage)"""
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """Get free space"""
        pass

    @abstractmethod
    def get_items(self) -> dict[str: int]:
        """Get items"""
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """Get unique items count"""
        pass



class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        """Initial
        :param items: - it is data to store in format of dict where key is title of commodity
        and value is quantity of the commodity
        :param capacity: - it is number of capacity of the storage
        """
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int):
        """Add a new item to the store"""
        if quantity < self.capacity:
            self.capacity -= quantity
            self.items[title] = quantity
        else:
            raise NotEnoughCapacity

    def remove(self, title: str, quantity: int):
        """Remove goddy from storage"""
        if quantity > self.items[title]:
            self.items[title] = 0
        else:
            self.items[title] -= quantity

    def get_free_space(self) -> int:
        """Get free space from storage"""
        return self.capacity

    def get_items(self) -> dict[str | int]:
        """Return a dict of all items in the store"""
        return self.items

    def get_unique_items_count(self) -> int:
        """Return quantity of uniq commodities"""
        return len(self.items.keys())
