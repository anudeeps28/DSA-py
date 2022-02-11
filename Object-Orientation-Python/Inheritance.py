# inheritance = 2 class similar, we don not need to write fully. 
# the similarities can be inherited from an upper level class


# being a noob coder:
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print("Bark")

# Doing what I did above while being a pro:
class Pet: # this is the master class (this is the general class)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("I don't know what I speak")
    
class Cat(Pet): # write Pet inside the brackets instead of self to use the functionallity of the Pet Class
                # this means that I am inheriting the upper level class pet
                # this is a more specific class, not a general class
                # these are also known as the child classes
    def __init__(self, name, age, color): # we need to change the color of our car, but not of dogs and fish
        super().__init__(name,age) # because these were defined in super class (the main general class, we need to take from there rather than copying the same 2 lines here as well. That will be wrong)
        self.color = color # additional attribute added
        #patent init (initialization) is important, so use that. Only when some additional attribute has to be added, then only use 
        #super init

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
    

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()    

c = Cat("Bill", 34, "Blue")
c.show()  # there is no method of show in Cat, but it inherits this from the master class Pet
        # also, it worked without definint the init method inside Cat
c.speak() 

d = Dog("Jill", 25)
d.show()
d.speak()   # if there is a method that is defined in both the general class and also the   
            # specific class, the program will take the specific class one.
            # but if the specific class does not have anything, then only it will go to the
            # general class one
f = Fish("Bubbles", 60)
f.speak() 