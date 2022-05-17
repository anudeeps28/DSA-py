# 1. List comprehension
# list comprehension provides us a way to transform one list to another

numbers = [1,2,3,4,5,6,7]
# printing even numbers
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
print(even)
# list comprehension =  a better way of doing this (in one line)
even2 = [i for i in  numbers if i%2 == 0]
print(even2)
# syntax is compact and much readable
# another example 
sqr_numbers = [i*i for i in numbers]
print(sqr_numbers)

# 2. Set comprehension
# set is an unordered collection of unique items (you cannot have same items, unlike list)
s = set([1,2,3,4,5,2,2,1]) # method - 1 of creating set
print(s)
# syntax for sets {}
# using comprehension
even3 = {i for i in s if i%2==0} # method - 2 of creating set
print(even3) 

# 3. Dictionary comprehension
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

# zip function = zips two lists together (creates tuples)
z = zip(cities,countries)
for a in z:
    print(a)

# making dictionary (dict comprehension)
d = {city:country for city,country in zip(cities,countries)}
print(d)
