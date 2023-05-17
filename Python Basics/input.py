username = input("Enter username:")
print("Username is: " + username)

# python 2.7 uses raw input
# username = raw_input("Enter username:")
# print("Username is: " + username)

### METHOD - 2 ###

# Read a line of space-separated integers from the user
input_str = input("Enter a line of integers: ")

# Split the input string into individual values and convert them to integers
arr = map(int, input_str.split())

# Print the resulting sequence of integers
print(list(arr))
