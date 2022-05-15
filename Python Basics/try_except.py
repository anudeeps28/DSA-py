# exception handling via try-except
from multiprocessing.sharedctypes import Value


x = input("Enter number1: ")
y = input("Enter Number2: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("exception occured: ", e)
    z = None
# except ValueError as e:
#     print("Exception Occured: ", e)
#     z = None
    # you can also write this as:
    # except ValueError as e:
        # print("Value Error exception")
    
# to know the type of exception
except Exception as e:
    print("exception type: ", type(e).__name__)
    z = None    

# once you know the type of exception, rewrite the except block and name the exception
print("Division is: ", z)


'''
In this when some error comes, you name that error as exception

The way is just to test and give exceptions by the name of the exceptions in terminal

If you need to take care of any uncommon exception, place it under an exceptio block
like
except Exception as e:
    print("exception:", e)
'''




