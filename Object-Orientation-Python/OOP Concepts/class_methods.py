# class attributes  

class Person:
    number_of_people = 0    # this is a class attribute(class variable)
                            # does not use self (so not a regular attribute)
                            # it is defined for the entire class; is the same of each object
                            # this is not going to change for each instance of the class
                            
    def __init__(self,name):
        self.name = name # this is an intance variable (not a class variable), 
                        # This is not shared by objects, every object has its own copy
        Person.add_person()
    # a class method can only access a class variable, not an instance variable
    @classmethod # we use this decorator directly above the method to show that it is a class method
    def number_of_people_(cls):  # this is a class method (not a regular method)
                                # this method will not be acting on one instance, this is meant to 
                                # act on the class itself. 
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("Bill")

print(p1.number_of_people) 
print(Person.number_of_people) # same as line 15, because number_of_people defind for the class, not an instance

Person.number_of_people = 8
print(p2.number_of_people) #changes to 8 even though we did not change it for p2 explicitly
Person.number_of_people = 9
print(p1.number_of_people) 

# classes are exportable, we can write it and export and use it at another place, and it will work the same way
# **********************************************************

print(Person.number_of_people_()) # this will display 2
