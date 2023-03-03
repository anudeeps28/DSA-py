# Finding the length of the array
arr = [1, 2, 3, 4, 5]
print(len(arr)) # Output: 5

# Adding an element to the end of the array
arr = [1, 2, 3, 4, 5]
arr.append(6)
print(arr) # Output: [1, 2, 3, 4, 5, 6]

# Removing the last element from the array
arr = [1, 2, 3, 4, 5]
arr.pop()
print(arr) # Output: [1, 2, 3, 4]

# Removing the element at index 1 from the array
arr = [1, 2, 3, 4, 5]
arr.pop(1)
print(arr) # Output: [1, 3, 4, 5]

# Sorting the array in ascending order
arr = [5, 2, 4, 1, 3]
sorted_arr = sorted(arr)
print(sorted_arr) # Output: [1, 2, 3, 4, 5]

# Sorting the array in descending order
arr = [5, 2, 4, 1, 3]
sorted_arr = sorted(arr, reverse=True)
print(sorted_arr) # Output: [5, 4, 3, 2, 1]

# Reversing the array
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr) # Output: [5, 4, 3, 2, 1]
