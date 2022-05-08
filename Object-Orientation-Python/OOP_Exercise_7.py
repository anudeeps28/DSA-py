'''

    Write a program to determine which class a given Bus object belongs to.


'''

class Vehicle:
    def __init__(self, name, milage, capcaity):
        self.name = name
        self.milage = milage
        self.capacity = capcaity

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 12, 50)

# showing the type (the class which it belongs to) of object School_Bus
print(type(School_Bus))


