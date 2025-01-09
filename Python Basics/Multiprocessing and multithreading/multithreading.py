'''

while a part of the program is waiting for something,
there can be other part of the program that can be processes
to save time and computation costs

'''

# program without multi-threading


import time

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2) # this will make the program wait for a 0.2 seconds before printing (we can see this as time sleeps for 0.2 seconds)
        print("Square:", n*n)
    
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube:", n*n*n)


array = [2,3,8,9]

t = time.time()
calc_square(array)
calc_cube(array)

print("done in", time.time() -t)
print("Hah... I am done with all my work now!")

# this program took 1.6 seconds
# you are first calculating square and then calculating cube
# but while you wait for 0.2 seconds, your CPU is idle, it is doing nothing
# multi threading tries to utilize this idle time and give CPU some work
print("########################################################################################")

# program with multi-threading (this will take less time)
import threading # this is the standard python module used for multi-threading

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2) # this will make the program wait for a 0.2 seconds before printing (we can see this as time sleeps for 0.2 seconds)
        print("Square:", n*n)
    
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube:", n*n*n)


array = [2,3,8,9]

t = time.time()

# what is a thread?
'''
Multiple threads live within the same process/program

Threads will have their own instruction set, their own stack memory, their own tasks
But they will be sharing is an address space
    * this means that any global variables defined in the program can be accessed by all of them

''' 

# creating threads which will run 
t1 = threading.Thread(target=calc_square, args=(array,))
t2 = threading.Thread(target=calc_cube, args=(array,))

# starting those threads
t1.start() # starting executing of squares calculation
t2.start() # at some other time, you started this before the completion of first thread

# when both are done, the come back and join to the main program  
t1.join() # join tells program that wail till this line until t1 is finished. don't go ahead of this
t2.join()

print("done in", time.time() -t)
print("Hah... I am done with all my work now!")

# now what it is doing is that it is not calculating these 2 functions in sequence
# it calculated square of first, and went into the loop and started waiting
# but because the other function was also calculating in parallel, it printed that
# this can also be seen in the result printed in the termainl
