# sharing data between 2 processes

from audioop import mul
from msvcrt import putch
import multiprocessing
import numbers

result = []

def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print("inside process" + str(result))


if __name__ == "__main__":
    numbers = [2,3,5]
    p = multiprocessing.Process(target=calc_square, args=(numbers, ))

    p.start()
    p.join()

    print("outside process" + str(result))

'''
The above program will give different results for outside and inside process

This is so because the new process gets its own area space

Solution = using shared memory

2 ways to share memory = using array and using value
'''

# sharing with array

def calc_square_arr(numbers,result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n
    

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array("i", 3)
    p = multiprocessing.Process(target=numbers, args=(numbers, result))

    p.start()
    p.join()

    print(result[:])

# sharing with value

def calc_square_arr(numbers,result, v):
    v.value = 5.57
    for idx, n in enumerate(numbers):
        result[idx] = n*n
    

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array("i", 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=numbers, args=(numbers, result))

    p.start()
    p.join()

    print(v.value)

# sharing data using queue

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)  

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, ))

    p.start()
    p.join()

    while q.empty() is False:
        pring(q.get())