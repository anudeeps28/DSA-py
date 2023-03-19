def swap(a,b,arr):
    arr[a], arr[b] = arr[b], arr[a] # python makes it easy to swap

def partition(elements, start, end):
    pivotIndex = start
    pivot = elements[pivotIndex]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, elements)
        
    swap(pivotIndex, end, elements)
    
    return end
    

def quickSort(elements, start, end): 
    if start < end:
        pi = partition(elements, start, end)
        quickSort(elements, start, pi-1) # left partition
        quickSort(elements, pi+1, end) # right partition

if __name__ == "__main__":
    
    # elements to be sorted
    elements = [11,9,29,7,2,15,28]
    
    quickSort(elements, 0, len(elements)-1)
    print(elements)