class Item:
    # every attribute takes "self" because the instance of the class is passed as the first argument
    def calculate_total_price(self, x, y): 
        return x * y

# creating an instance of the class
item1 = Item()

# assigning attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# calling methods from instance of the class
print(item1.calculate_total_price(item1.price, item1.quantity))


# We could create as much as instances we'd like to
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))
