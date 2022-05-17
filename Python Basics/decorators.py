'''
Functions can be passed as arguement to another function 
and also
they can even be returned as a return value

In short, we can use them like variables
'''

import time

from pkg_resources import resource_listdir

def time_it(func):
    def wraper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took" + str((end-start)*1000) + "mil sec to complete")
        return result

    return wraper

@time_it # this is the decorator
def cal_square(numbes):
    result = []
    for number in numbers:
        result.append(number*number)
    
    return result

@time_it # this is the decorator
def cal_cube(numbes):
    result = []
    for number in numbers:
        result.append(number*number*number)
    
    return result

array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)

'''
the decorator helps us use the function without interfering with the logic of the main code
'''