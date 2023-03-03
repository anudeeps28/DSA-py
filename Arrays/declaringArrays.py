# Creating a one-dimensional array of integers
arr = [1, 2, 3, 4, 5]

# Creating a one-dimensional array of strings
arr = ['apple', 'banana', 'cherry']

# Creating a two-dimensional array of integers
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# Creating a two-dimensional array of strings
arr = [['apple', 'banana', 'cherry'],
       ['orange', 'pear', 'grape'],
       ['watermelon', 'pineapple', 'kiwi']]

# Accessing the first element in the array
arr = [1, 2, 3, 4, 5]
print(arr[0]) # Output: 1

# Accessing the third element in the array
print(arr[2]) # Output: 3

# Accessing the element in the first row and second column
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(arr[0][1]) # Output: 2

# Accessing the element in the third row and third column
print(arr[2][2]) # Output: 9

# Modifying the second element in the array
arr = [1, 2, 3, 4, 5]
arr[1] = 10
print(arr) # Output: [1, 10, 3, 4, 5]

# Modifying the element in the second row and third column
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
arr[1][2] = 10
print(arr) # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
