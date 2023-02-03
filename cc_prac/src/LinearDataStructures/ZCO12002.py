# https://www.codechef.com/problems/ZCO12002

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
    
def binarysearchstart(arr , bound, pos):
    beg = 0
    end =  pos - 1
    val = -1
    while beg<=end:
        mid = floor((beg+end) / 2)
        if arr[mid] <= bound:
            val = arr[mid]
            beg = mid+1
        else:
            end = mid-1 
    return val

def binarysearchend(arr , bound, pos):
    beg = 0
    end =  pos - 1
    val = -1
    while beg<=end:
        mid = floor((beg+end) / 2)
        if arr[mid] >= bound:
            val = arr[mid]
            end = mid-1
        else:
            beg = mid+1 
    return val

n, x, k = mapintinp()
contest = []
for i in range(n):
    contest.append(lstintinp())
vworm = lstintinp()
wworm = lstintinp()

# print(contest)

vworm.sort()
wworm.sort()

res = float('inf')
for i in contest:
    t1 = binarysearchstart(vworm, i[0], x)
    t2 = binarysearchend(wworm, i[1], k)

    if ((t1 != -1) and (t2 != -1)):
        res = min(res, (t2 - t1 + 1))
    
print(res)