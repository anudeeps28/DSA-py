# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing dictionary elements
print(my_dict['name'])  # Output: John

# Adding an element to the dictionary
my_dict['phone'] = '123-456-7890'

# Removing an element from the dictionary
del my_dict['age']

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)

############################################################

# Create a new dictionary
d = {}

# Add some key-value pairs
d["apple"] = 1
d["banana"] = 2
d["cherry"] = 3

# Retrieve a value by key
print(d["banana"])   # Output: 2

# Check if a key is in the dictionary
if "apple" in d:
    print("Apple is in the dictionary")

# Remove a key-value pair
del d["banana"]
