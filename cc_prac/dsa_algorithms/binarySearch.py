# Prefer iterative method over recursive
# https://stackoverflow.com/questions/57481997/recursive-and-iterative-binary-search-which-one-is-more-efficient-and-why

# Time complexity for both recursive and iterative is O(logn)
# but space complexity is O(1) for iterative and O(logn) for recursive

def binary_search_recursive(A,low,high,key): #needs a sorted array and binary_search(Array_name, first_index, last_index, element_to_be_found)
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
            return binary_search_recursive(A, low, mid-1, key)
        else:
            return binary_search_recursive(A, mid+1, high, key)
    

def binary_search_iterative(A,low,high, key): #needs a sorted array and binary_search(Array_name, first_index, last_index, element_to_be_found)

    while(low<=high):
        mid = (low+high)//2
        if key==A[mid]:
            return mid
        elif key>A[mid]:
            low = mid+1
        else:
            high=mid-1
    return 'Element not Found'

A = [1,5,4,3,7,544,67,88,2]
A.sort()
c = binary_search_iterative(A,0, len(A)-1,88)
print(c)