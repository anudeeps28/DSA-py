import time
import multiprocessing # multiprocessing module in python 

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(5) 
        print("Square:", n*n)
    
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(5)
        print("Cube:", n*n*n)


if __name__ == "__main__":
    array = [2,3,8,9]

    t = time.time()

    # creating processes 
    p1 = multiprocessing.Process(target=calc_square, args=(array,))
    p2 = multiprocessing.Process(target=calc_cube, args=(array,))

    # same start call as threading 
    p1.start() 
    p2.start() 

    # same join call as threading
    p1.join() 
    p2.join()

    print("done in", time.time() -t)
    print("Hah... I am done with all my work now!")

# you can go and see these 2 processes being implemented in the activity monitor/task manager

