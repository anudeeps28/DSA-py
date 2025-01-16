# classes that organize functions together
# we want to organize the functions into a class, so that they stay structured 
# and we can move all the classes to a new module and they continue to work the say way

class Math:
    
    @staticmethod   # these method do not have access to instance like normal methods
                    # all they do is something. They do something but don't change anythying
    def add5(x):    # because this is not a normal method, we don't need to declare any self, etc. It does not need anything
        return x + 5

    @staticmethod
    def pr():
        print("run")

print(Math.add5(6))
print(Math.pr())