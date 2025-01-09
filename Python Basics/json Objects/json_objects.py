# creating an address book and saving as file on computer
book = {} # there is no json object in python, only lists, strings, dict etc

book [ "tom"] = {
    "name": "tom",
    "address": "1 street",
    "phone": 5645
}

book [ "bob"] = {
    "name": "bob",
    "address": "2 street",
    "phone": 734924
}

import json
s = json.dumps(book) # dumping book dictionary as a string and converting into a json format
print(s)

# saving this on the local computer
with open ("python_sample_book.txt", "w") as f: # w for writing
    f.write(s)
# this has saved the file on computer
# now you can write any program to read from this file

print("///////////////////////////////////////////////////////////")


# read the address book and print the address book recored
f = open("python_sample_book.txt", "r") # r for reading
s = f.read()
print(s)

import json
book_2 = json.loads(s) # converts the string into a dictionary
print(book_2)  
print(type(book_2))

# now searching in a dictionary is super easy (this is the power of json and dictionaries)
# finding bob's entire recore
print(book["bob"])

# bob's phone number
print(book["bob"]["phone"])

# printin all records
for person in book:
    print(book[person])

