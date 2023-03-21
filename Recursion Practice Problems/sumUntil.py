def sumUntil(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return n + sumUntil(n-2)

if __name__ == "__main__":
    n = 10
    print(sumUntil(n))