# one child class inheriting from 2 or more parent classes
class Father():
    def gardening(self):
        print("I enjoying gardening")

class Mother():
    def cooking(self):
        print("I enjoy cooking")

class Child(Father,Mother): # thus child will have access to gardening and cooking method as well
    def sports(self):
        print("I enjoy sports")

c = Child() 
c.gardening()
c.cooking()
c.sports()

# the child has access to its own method as well as its parent class method


print("////////////////////////////////////////////")


# another use case of multiple inheritence
class Father():
    def skills(self):
        print("programming, gardening")

class Mother():
    def skills(self):
        print("cooking, art")

class Child(Father,Mother): # thus child will have access to gardening and cooking method as well
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sports")

c2 = Child()
c2.skills()