from enum import Enum, auto


class Item(Enum):
    """Item type"""

    APPLE = auto()
    ORANGE = auto()
    BANANA = auto()
    CHOCOLATE = auto()
    CANDY = auto()
    GUM = auto()
    COFFEE = auto()
    TEA = auto()
    SODA = auto()
    WATER = auto()

    def __str__(self):
        return self.name.upper()


class ShoppingCart:
    """
    Simple Shopping App that lets us

        - Add items to the cart
        - Remove items from the cart
        - Calculate the total based on the quantity
        - View cart items
        - Clear cart
    """

    def __init__(self):
        """
        Creates a shopping cart object with an empty dictionary of items
        """
        self.items = {}

    def add_item(self, item: Item, price: int | float, quantity: int = 1) -> None:
        """
        Adds an item to the shopping cart
        :param quantity: Quantity of the item
        :param item: Item to add
        :param price: Price of the item
        :return: None
        """
        if item.name in self.items:
            self.items[item.name]["quantity"] += quantity
        else:
            self.items[item.name] = {"price": price, "quantity": quantity}

    def remove_item(self, item: Item, quantity: int = 1) -> None:
        """
        Removes an item from the shopping cart
        :param quantity: Quantity of the item
        :param item: Item to remove
        :return: None
        """
        if item.name in self.items:
            if self.items[item.name]["quantity"] <= quantity:
                del self.items[item.name]
            else:
                self.items[item.name]["quantity"] -= quantity

    def get_total_price(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def view_cart(self) -> None:
        """
        Prints the contents of the shopping cart
        :return: None
        """
        print("Shopping Cart:")
        for item, price in self.items.items():
            print("- {}: ${}".format(item, price))

    def clear_cart(self) -> None:
        """
        Clears the shopping cart
        :return: None
        """
        self.items = {}
