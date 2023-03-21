'''
Write a Python program to calculate the sum of a list of numbers
'''
def calculateSum(numbers):
    for i in numbers:
        if len(numbers) == 1:
            return numbers[0]
        return numbers[0] + calculateSum(numbers[1:])

if __name__ == "__main__":
    numbers = [2, 4, 5, 6, 7]
    print(calculateSum(numbers))