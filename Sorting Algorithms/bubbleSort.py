def bubbleSort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False # to check if we swapped any element in first iteration, if not, the array is already sorted, and we won't do it again and again
        for j in range(size-1-i): # if the last 2 elements are sorted, so you don't go there only
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

            if not swapped:
                break

if __name__ == "__main__":
    
    # elements to be sorted
    elements = [5,9,2,1,67,88,34]
    
    # strings can also be sorted using this
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    
    bubbleSort(elements)
    print(elements)