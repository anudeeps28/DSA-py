from item import Item

class Keyboard(Item):
    pay_rate = 0.7 # changing payrate in this class
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
