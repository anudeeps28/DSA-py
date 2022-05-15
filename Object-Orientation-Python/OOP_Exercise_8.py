'''
 Determine if School_bus is also an instance of the Vehicle class

'''

class Vehicle: 
    def __init__(self, name, milage, capacity):
        self.name = name
        self.milage = milage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 12, 50)

# ininstance() function built-in python
print(isinstance(School_Bus, Vehicle)) #true because this is an instance variable of class Vehicle
print(isinstance(Bus, Vehicle)) #false becuse bus not a variable, it is a sub-class

# issubclass() = tells if one class is a subclass of another class or not
print(issubclass(Bus,Vehicle))
