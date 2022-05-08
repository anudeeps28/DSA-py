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
