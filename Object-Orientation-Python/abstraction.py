from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,x):
        print ("passed value: ", x)
    
    @abstractmethod
    def task(self):
        print("we are insde the Absclass task")

class test_class(Absclass):
    def task(self):
        print("we are inside the test_class tast")

class example_calss(Absclass):
    def task(self):
        print("we are inside the example_class task")

# object of test class created
test_obj = test_class()

# object of example class created
example_obj = example_calss()

# calling methods

# these invoke the task methods of individual sub-classes
test_obj.task() 
example_obj.task()

# this invokes the print method of the main class (since it is not an abstract method)
test_obj.print(100)
example_obj.print(200)



