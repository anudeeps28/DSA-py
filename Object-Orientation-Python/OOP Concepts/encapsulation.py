# demonstrating encapsulation

class Base:
    def __init__(self):

        # protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        # constructor of base class
        Base.__init__(self)
        print("Calling the protected member of base class-", self._a)

        # modifying the protected variable
        self._a = 3
        print("Calling modified protected member outside class-", self._a)

obj1 = Derived()
obj2 = Base()

# calling protected members

print("accessing protected member of obj1", obj1._a) # this can be done, but is not usually done due to convention
print("accessing protected member of obj2", obj2._a) # accessing protected variable outside

# another classic example
class Payment:
    def __init__(self,price):
        delf.__final_price = price + price * 0.05 # .__ = private variable = you cannot access it. it will give error. So we need getters and setters to get it
        
    # getter function (this is just a wrapper to get the final price)
    def get_final_price(self):
        return self.__final_price
    
    # but if you want to change final price variable, you use this function. any other change apart from this function will not work
    def set_final_price(self, discount):
        self.__final_price =  self.__final_price - (self.__final_price * (discount/100))
    
book = Payment(10)

# now if we try to change the variable = it does not affect
book.__final_price = 0 # this will simply not work 

# but this will work because this is setter function 
book.set_final_price(10)

print(book.get_final_price())

# this way, we can change the variable inside the class but we cannot directly change the variable
# this is how encapsulation works = making items private or public
