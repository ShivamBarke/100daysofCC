# https://docs.python.org/3/library/collections.html
from collections import *

# https://docs.python.org/3/library/math.html
from math import ceil, floor, fsum, gcd, lcm, factorial, perm, comb, log, log2, log10, pow, sqrt

def inp():
    return input().rstrip()

def intinp():
    return int(input().rstrip())

def mapintinp():
    return map(int, input().split())

def lstintinp():
    return list(map(int, input().split()))

def lstinp():
    return list(input().split())

def total(iterable):
    return fsum(iterable)


def binary_search(A,low,high, key): #needs a sorted array and binary_search(Array_name, first_index, last_index, element_to_be_found)

    while(low<=high):
        mid = (low+high)//2
        if key==A[mid]:
            return mid
        elif key>A[mid]:
            low = mid+1
        else:
            high=mid-1
    return 'Element not Found'

