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

# checking if some person name is in dictionary or not
if "tom" in d:
    print("yes")

# trash all entries from your dict
d.clear()

print("///////////////////////////////////////////////////////////")

# tuples = list of values grouped together
point = (5,9) # defining a tuple
print(point[1])

# another example of tuple
address = ("282 Littleton St.", "Crestview NorthApartments", 47906)
# you access items in a tuple just like a list
for i in address:
    print(i)

# we can create a list of tuples
list_of_tuples = [(4,5), (4,7), (7,8)]

