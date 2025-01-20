import csv

class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute in the constructor
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # Count out the floats that are point zero (i.e. 10.0, 5.0)
        if isinstance(num, float):
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False

    # __repr__ is a magic function in python used to represent the class
    def __repr__(self):
        return f"Item'{self.name}', {self.price}, {self.quantity}"

Item.instantiate_from_csv()
print(Item.all)
