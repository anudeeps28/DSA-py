def calculateSum(n):
    if n == 0:
        return 0
    return n%10 + calculateSum(n//10)

if __name__ == "__main__":
    digit = 345
    print(calculateSum(digit))