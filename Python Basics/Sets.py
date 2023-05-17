### CREATING A SET ###

# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3}

### SET OPERATIONS ###

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


### MODIFYING A SET ###

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

### SET MEMBERSHIP
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True

### ITERATING OVER A SET
my_set = {1, 2, 3}
for element in my_set:
    print(element)
# Output:
# 1
# 2
# 3
# we cannot use an index to iterate over a set, like we can do in a list!