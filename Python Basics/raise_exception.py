# 1. how to raise standard exceptin
from ast import expr_context


try:
    raise MemoryError ("Memory Error") # in place of memory error, you can write the name of any standard exception
except MemoryError as e:
    print(e)

print("#####################################################")

# 2. how to raise a user defined exception
# we want to raise our own user-defined exception
'''
    Exception in python as instances of classes
    do define your own exception = you need to define your own class
'''
class Accident(Exception):# every exception you define has to be derived from the base class Exception
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ", self.msg)
# now raising the exception
try:
    raise Accident("crash between 2 cars")
except Accident as e:
    e.print_exception()

print("#####################################################")

# 3. finally statement
# this is used to do clean up
# every code inside finally will work, no matter what 

def process_file():
    try:
        f = open("writing_file.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("closing resources")
        f.close

process_file()
# even when the exception happens inside the try - except block and even if there is no handling of that excption
# then also the stuff in finally block executes

