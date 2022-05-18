'''

This function returns the minimum number of operations
required to make all elements in an array equal.

We are given an array consisting of n elements. 
At each operation you can select any one element and 
increase rest of n-1 elements by 1. You have to make 
all elements equal performing such operation as many times you wish. 
Find the minimum number of operations needed for this.
'''

# brute force approach
'''
A simple way to make all elements equal is that at each step 
find the largest elements and then increase all rest n-1 elements by 1.
We should keep doing this operation till all elements become equal. 
Time Complexity : O(n^2)
'''

# better solution
'''
If we took a closer look at each operation as well problem statement 
we will find that increasing all n-1 element except the largest one 
is similar to decreasing the largest element only.

So, in order to do this(decreasing only the largest element), we need to
understand that the smallest element will not decrease, while all the 
othe elements will decrease by -1 in every iteration until they all become
equal to the smallest.

To achieve this:
    * we take the given array
    * we subtract the smallest from each element
    * this gives us a new matrix
    * we add up all the elements of this new matrix
    * this is our solution

We get this by operating (sum_of_array - (smallest * number of elements))
Hence, the logic

Time Complexity : O(n)
'''
def countOperations(counters):
    num_elements = len(counters)

    arr_sum = sum(counters)

    return arr_sum - (num_elements * min(counters))


if __name__ == "__main__":
    print(countOperations([3,4,6,6,3]))
