def power(a,b):
    if b == 0:
        return 1
    return a * power(a, b-1)

if __name__ == "__main__":
    a = 3
    b = 4
    print(power(a,b))