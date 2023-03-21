'''
Write a Python program to get the factorial of a non-negative integer. 
'''
def factorial(n):
    if n < 0:
        return
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = 5
    print(factorial(n))