def binary_search(A,low,high,key): #needs a sorted array and binary_search(Array_name, first_index, last_index, element_to_be_found)
    if (low>high):
        if(A[low]==key):
            return low
        else:    
            return 'Element not found'
    else:
        mid = (low+high)//2
        if(key==A[mid]):
            return mid
        elif (key<A[mid]):
            return binary_search(A, low, mid-1, key)
        else:
            return binary_search(A, mid+1, high, key)
    

A = [33]
A.sort()
print(A)
c = binary_search(A, 0, len(A)-1, 21)
print(c)