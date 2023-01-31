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
    return int(fsum(iterable))


#https://www.codechef.com/problems/NOTALLFL
for _ in range(intinp()):
    # n = intinp()
    n, k = mapintinp() #5, 3

    A = lstintinp()  #[1, 1, 2, 2, 1]

    flav = [-1]*k #[-1,-1,-1]
    t = 0

    for i in range(n):
        flav[A[i]-1] = i

        if -1 in flav:
            t+=1
        else:
            t = max(t, i-min(flav))

    print(t)

