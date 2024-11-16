from datetime import datetime

class Product:
    def __init__(self, name="Unnamed", price=0, quantity=1):
        if 3 <= len(name) <= 8:
            self._name = name
        else:
            raise ValueError("Name must be between 3 and 8 characters")

        self._price = max(price, 0)
        self._quantity = max(quantity, 1)
        
        print(f"Product created: {self._name} - {datetime.now()}")

    def get_total_price(self):
        return self._price * self._quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 8:
            self._name = value
        else:
            raise ValueError("Name must be between 3 and 8 characters")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Quantity must be at least 1")

    def __str__(self):
        return f"Product(name={self._name}, price={self._price}, quantity={self._quantity})"
