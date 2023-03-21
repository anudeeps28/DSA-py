'''
Write a Python program to sum recursion lists. 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21'''

def calculateSum(numbers):
    result = 0
    for i in numbers:
        if type(i) == int:
            result = result + i
        
        if type(i) == type([]):
            result = result + calculateSum(i)
    
    return result

        

if __name__ == "__main__":
    data = [1, 2, [3,4], [5,6]]
    print(calculateSum(data))