# Finding the maximum and minimum elements in the array
arr = [5, 2, 4, 1, 3]
max_element = max(arr)
min_element = min(arr)
print(max_element) # Output: 5
print(min_element) # Output: 1

# Finding the sum of elements in the array
arr = [1, 2, 3, 4, 5]
sum_of_elements = sum(arr)
print(sum_of_elements) # Output: 15

# Finding the index of the element 3 in the array
arr = [1, 2, 3, 4, 5]
index_of_element = arr.index(3)
print(index_of_element) # Output: 2

# counting occurances of an element
arr = [1,2,3,4,5,4,6,2,1]
countOfElements = arr.count(3)
print(countOfElements) # Output: 2

# Removing duplicates from an array
arr = [1,1,2,1,4,3,5,32,2,1]
uniqueArr = list(set(arr)) # using a set
print(uniqueArr) # Output: 1,2,3,4,5,32

# Finding intersection and union of two arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
intersection = list(set(arr1).intersection(arr2))
union = list(set(arr1).union(arr2))
print(intersection) # Output: [3, 4, 5]
print(union) # Output: [1, 2, 3, 4, 5, 6, 7]

# Rotating the array by 2 positions to the left
arr = [1, 2, 3, 4, 5]
rotated_arr = arr[2:] + arr[:2] # elements(3->5) + elements(1->2)
print(rotated_arr) # Output: [3, 4, 5, 1, 2]
