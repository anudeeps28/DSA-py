# defining the class
class Item:
    def __init__(self, name:str, price: float, quantity = 0):
        # assign self to object
        self.name = name # these are instance attributes 
        self.price = price
        self.quantity = quantity

        # validate the received arguments
        assert price >= 0, f"Price {self} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1) # creating an instance of the class
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price()) 
print(item2.calculate_total_price())
