# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# given
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers" # this is actually a pro way to add print instead of using the conventional print

    
class Bus(Vehicle):
    # assigning default capacity 
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity) # In child class, we can refer to parent class by using the super() function. 

# making variable
School_Bus = Bus("School Volvo", 180, 20)
print(School_Bus.seating_capacity())
