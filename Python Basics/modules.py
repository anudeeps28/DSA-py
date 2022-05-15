# modules = reusing the code written by someone else
import math # in built python module
print(math.sqrt(16))
print(dir(math))

# google for all python modules 
print(math.pi)

# import calendar module
import calendar
cal = calendar.month(2016,1) # printint one month 
print(cal)

print(calendar.isleap(2016)) # is leap is a command in claendar module

# writing own module (in my_module.py) and importing in this
import my_module # can also do import my_module as m and then call as m.calculate_square_area
area = my_module.calculate_square_area(5)
print(area)

''' 
if my_module is not in same directory:
    we need to give the address (system path)

using
sys.path.append("C:/Code")
import my_module as m
area = m.calculate_square_area(10)
'''



