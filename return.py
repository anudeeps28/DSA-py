def return_42():
    return 42  # An explicit return statement
...

return_42()  # The caller code gets 42
42

# ///

num = return_42()
num


return_42() * 2


return_42() + 5

# ///

def get_even(numbers):
    even_nums = [num for num in numbers if not num % 2]
    return even_nums


get_even([1, 2, 3, 4, 5, 6])

# ///

def get_even(numbers):
    return [num for num in numbers if not num % 2]


get_even([1, 2, 3, 4, 5, 6])

# ///

def mean(sample):
    return sum(sample) / len(sample)


mean([1, 2, 3, 4])

# ///

def add_one(x):
    # No return statement at all
    result = x + 1


value = add_one(5)
value

print(value)

# ///

return_value = print("Hello, World")


print(return_value)

# ///

def print_greeting():
    print("Hello, World")


print_greeting()


def return_greeting():
    return "Hello, World"


return_greeting()

# ///

def print_42():
    print(42)


print_42()


def return_42():
    return 42


return_42()

# ///

def add(a, b):
    result = a + b
    return result

add(2, 2)

# ///

def add(a, b):
    result = a + b
    return result

print(add(2, 2))

# ///

import statistics as st

def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample)

# ///

sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
mean, median, mode = describe(sample)

mean


median


mode


desc = describe(sample)
desc


type(desc)

# ///

divmod(15, 3)


divmod(8, 3)

# ///

def omit_return_stmt():
    # Omit the return statement
    pass

print(omit_return_stmt())


def bare_return():
    # Use a bare return
    return

print(bare_return())


def return_none_explicitly():
    # Return None explicitly
    return None

print(return_none_explicitly())

# ///

def template_func(args):
    result = 0  # Initialize the return value
    # Your code goes here...
    return result  # Explicitly return the result

# ///



