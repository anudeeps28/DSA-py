# define a property that must have the same value for every class instance (object)


from OOP_Exercise_3 import School_Bus


class Vehicle:
    # giving global variable (this will be the same for every class and function)
    color = "White"

    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)
print(School_Bus.color, School_Bus.name,"Speed: ", School_Bus.max_speed,"Milage: ", School_Bus.milage)