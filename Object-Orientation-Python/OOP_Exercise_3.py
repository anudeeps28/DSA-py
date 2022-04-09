# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# Given
class Vehicle: # this is the main class (the parent class)

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle): # this is the child class of vehicle
    pass

School_Bus = Bus("Volvo Bus", 180, 20 )
print("School Bus:", School_Bus.name, "max speed:", School_Bus.max_speed, "milage:", School_Bus.mileage)

