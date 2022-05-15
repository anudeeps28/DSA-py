# writing a class

from unicodedata import name


class Human: # this is how we define class
    def __init__(self, n, o): # this is a special function we define everytime we define a class
        '''
        This function will initialize the properties of the class that will be 
        used when we use instances of this class
        '''
        # self = is this class (a syntax - type)

        # these are the properties of Human
        self.name = n
        self.occupation = o

    # all the other functions after this are methods
    # these are the actual functions that will do the work

    def do_work(self): # first argument in any method = self
        if self.occupation == "tennis_player":
            print(self.name, "tennis player")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")
    
    def speaks(self):
        print(self.name, "says how are you?")

# this is the end of class

# now we create instances of the class
tom = Human("tom cruise", "actor")

# calling methods
tom.do_work()
tom.speaks()

# creating another instance
maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()

# when writing large programs, it is important to write programms
# in classes (object oriented programming)
# OOP makes life very easy while writing large programs

