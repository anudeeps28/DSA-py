### DICTIONARY = MAPS ###
# dictionary = telephone directory
d = {"tom": 462239, "rob":7493272349, "joe":46294723} # making a dictionary

# retrieving value from dictionary using its key
print(d["tom"])

# adding new entry in dictionary
d["sam"] = 977957439
print(d)

''' 
* the order does not matter in dictionaries
* sole purpose of dictionary is to access value using its key
'''

# delete an entry from a dictionary
del d["sam"]
print(d)

# how to print all directory(dictionary) values
for key in d:
    print("key:", key, "value:", d[key])

# printing all values using tuple
for k,v in d.items(): 
    print("key:", k, "value:", v)
    
# printing only the values
for value in d.items():
    print("value:", value)

# checking if some person name is in dictionary or not
if "tom" in d:
    print("yes")

# trash all entries from your dict
d.clear()

print("///////////////////////////////////////////////////////////")

### TUPLES = immutable lists ###

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6
mixed_tuple = ('apple', 1, True)


# tuples = list of values grouped together
point = (5,9) # defining a tuple
print(point[1])

my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# another example of tuple
address = ("282 Littleton St.", "Crestview NorthApartments", 47906)
# you access items in a tuple just like a list
for i in address:
    print(i)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will result in an error

my_tuple = (10, 2, 3)  # Create a new tuple and assign it to the same variable

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
print(my_tuple.index(3))  # Output: 3


# we can create a list of tuples
list_of_tuples = [(4,5), (4,7), (7,8)]
