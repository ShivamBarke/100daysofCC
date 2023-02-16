# Prefer iterative method over recursive
# https://stackoverflow.com/questions/57481997/recursive-and-iterative-binary-search-which-one-is-more-efficient-and-why

# Time complexity iterative binary sort is O(n^2)
# https://www.interviewkickstart.com/learn/binary-insertion-sort#:~:text=For%20average%2Dcase%20time%20complexity,%CE%B8(N%5E2).

def binary_search_iterative(A,low,high, key): #needs a sorted array and binary_search(Array_name, first_index, last_index, element_to_be_found)

    while(low<=high):
        mid = (low+high)//2
        if key==A[mid]:
            return mid+1
        elif key>A[mid]:
            low = mid+1
        else:
            high=mid-1
    return low

def binary_sort(A):
    n = len(A)
    for i in range(n):
        key = A[i]

        index = binary_search_iterative(A,0, i-1, key)

        while (i-1 >= index):
            A[i] = A[i-1]
            i = i-1
        A[i] = key


A = [3.2,321.31,313.44]
binary_sort(A)
print(A)

