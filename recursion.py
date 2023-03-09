def findSum(n):
    # the base condition
    if n == 1:
        return 1
    # the recursion
    return n + findSum(n-1)

if __name__ == "__main__":
    print(findSum(5))