#Object Orientation Programming in Python

x = 1 #x = an object which is 1 (and that object is of the class int)
print(type("hello")) #the result of this shows that hello is an object of the class str (i.e. string)
print(type(x)) # --> x is an object of class int

#defining function and then finding its class
def hello(): 
    print("Hello")
print(type(hello)) # has class function 

# everything is an object of some kind of class, and that class defines how 
# that object can interact with other objects in our program

# this will give error because of different class types
# x = 1, y = hello, print (x+y). the type we declare defines how that thing can interact 

# METHODS
    # . followed  by () means some method is acting on an object
string = "hello"
print(string.upper()) #method upper acting on object stored in string

    # print(x.upper()) will give error





