# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# making the class
from ast import Mod


class Vehcile:
    def __init__(self,max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

# declaring variable (object) of the class
ModelX = Vehcile(240, 18)

#printing
print(ModelX.max_speed, ModelX.milage)

