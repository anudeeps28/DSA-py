class MyClass:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return MyClass(self.x + other.x)

a = MyClass(1)
b = MyClass(2)
c = a + b    # c.x == 3
