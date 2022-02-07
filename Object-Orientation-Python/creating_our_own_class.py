
from unicodedata import name


class Dog: 
    # creating a class dog means that I am in control of all the objects of class dog
    # also defining the operations that a dog can do  
    def __init__(self, name): # init method (this is a special method)
        # this allows us to instintiate the object right when it is created
        self.name = name # created an attribute name of class Dog  
        print(name)
        pass

    #method = a function that goes inside of a class
    
    def bark(self): # defining a method
        print("bark")
    
    def meow(self):
        return "meow"
    
    def add_one(self, x):
        return x+1

d = Dog("tim") # variable d assigned to an instance of the class dog
            #
print(type(d)) # gives the output <class '__main__.Dog'> 
    #__*****__ shows which module the class was defined in, which is 
    # main by default
print("/////////////////////")

#for using a method on an instance of the class:
d.bark() # calling method bark on object of class dog
print("/////////////////////")


print(d.add_one(5))
print("/////////////////////")

d2 = Dog("Bill") 
print("/////////////////////")
 # 2 different dog objects one names tim and other names bill and they both stored different names on their instances
# this is because of the self that we declared in init = stores permanently for each of the objects

print (d.name)
print (d2.name)
print("/////////////////////")


