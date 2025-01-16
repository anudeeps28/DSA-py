# understanding class, attributes and objects
# this is the blue print of how a class works, methods, attributes

class Dog: 
    # creating a class dog means that I am in control of all the objects of class dog
    # also defining the operations that a dog can do  

    # these attributes that are in the __init__ method have to be defined for every object. They are like nouns

    # this __init__ is also called the constructor, while the rest of the methods are called instance methods
    def __init__(self, name, age): # init method (this is a special method)
        # this allows us to instintiate the object right when it is created
        self.name = name # created an attribute name of class Dog   
        self.age = age  # we have added this new attribute, so every time we 
                        # add an object, we need to define both name and age
                        # but since this is a new attribute, we need to add 
                        # a new method to print this. Old pring will only print the name
        pass

    #method = a function that goes inside of a class
    # these methods can act on any of the objects, but may also not act. The are like verbs. They do something on object. The take action
    # But the __init__ attributes have to be defined for all objects
    def bark(self): # defining a method
        print("bark")
    
    def meow(self):
        return "meow"
    
    def add_one(self, x):
        return x+1
    # self.something = some value: we can reference them later on
    def get_name(self): # first arguement is always self (because we need to invisibly pass the dog object so
                        # sop that we know which dog we are accessing when we are goin to get
                        # say the name of the dog)
        return self.name
    
    def get_age(self): # will give error if self is not written inside ()
                       # error: TypeError: get_age() takes 0 positional arguments but 1 was given
        return self.age
    
    def set_age(self, age): #method to chane the attributes or create new attributes
        self.age = age

# creating instance variable for class 
# instance variable is nothing but when we make a variable that takes all the properties that we define in a class.
d = Dog("tim", 34) # variable d assigned to an instance of the class dog
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

d2 = Dog("Bill", 12) #another object defined for class Dog
print("/////////////////////")
 # 2 different dog objects one names tim and other names bill and they both stored different names on their instances
# this is because of the self that we declared in init = stores permanently for each of the objects

#we have 2 different dog objects, and they both store difference names in their instance
print (d.name)
print (d2.name)

print("/////////////////////")

print (d.get_name()) #this is the basics behind objects
print(d2.get_name())
print("/////////////////////") 

print (d.get_age()) #
print(d2.get_age()) 
print("/////////////////////") 

d.set_age(23)
print (d.get_age())
print("/////////////////////") 

# so we can modify and access these attributes inside of our class
# ////////////////////////////////////////////////////////////////

# Whey Object Oriented Programming?
# Once you have a class set up, you can have infinite amount of instances of it

#this is noob programming: not feasible when I need to make 25,000 of such things
dog1_name = "tim"
dog1_age = 34

# are lists substitutes?
# this is a pain, what if we need to access something from this data and especially 
# when there are 30 - 40 attributes of these. this is time consuming: using index and all
# also, what if we need to delete something: we need to find index and all the lists
# this is how onject oriented style makes sense
dogs_name = ["tim", "bill"]
dogs_age = [32,14]


