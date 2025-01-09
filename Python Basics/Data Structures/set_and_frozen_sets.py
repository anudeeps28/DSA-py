# 1. initializing a set (method -1)
basket = {"orange","apple", "mango", "apple", "orange"}
print(type(basket))
print(basket) # orange was present 2 times when we defined, but it is printed only once
# a set does not allow duplicate elements (it allows only unique elements)

# 2. another way of initializing set (method - 2)
a = set()
a.add(1)
a.add(2)
print(a)

# warning = only {} means a dictionary
b = {}
print(type(b))

''' 
A set is unordered, so we cannot use index to access. (But we can iterate over then and print)
This is the basic difference between a list and a set
'''

# set used to remove duplicate elements from a list (and set supports taking list as an input)
x = [1,2,3,4,2,3,4]
unique_x = set(x)
print(unique_x)

# you can always add new elements to that set
unique_x.add(9)
print(unique_x)

'''
Often, there are needs that you need your set to be frozen 
i.e. you don't want the content to be changed.

That is when frozen set comes into play
'''

# 4. initializing a frozen set
fs = frozenset(x) # takes input in the form of list
print(fs) 

# 5. basic set operations
x = {"a", "b", "c"}

# in 
print("a" in x)
print("g" in x)

# iteration
for i in x:
    print(i)

# defining another set
y = {"a", "g", "h"}

# union of sets
print(x|y) # OR operator

# intersection of sets
print(x&y) # AND operator

# difference of sets
print(x-y)

# finding if x is subset of y
print(x<y) # False because x is not a subset of y

z = {"h", "g"}
print(z<y) # True because z is a subset of y

