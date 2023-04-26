name = "John"
age = 30
print(f"My name is {name} and I'm {age} years old.")


name = "John"
age = 30
with open('output.txt', 'w') as f:
    f.write("My name is {} and I'm {} years old.".format(name, age))

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("The number is {}.".format(num))
