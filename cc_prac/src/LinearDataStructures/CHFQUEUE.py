# https://www.codechef.com/problems/CHFQUEUE

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

n, k = mapintinp()
A = lstintinp()
mod = 1000000007

stack = []
fear = 1

for i in range(n):
    while len(stack)>0 and A[stack[-1]]>A[i]:
        fear = fear*(i-stack[-1]+1)
        stack.pop()

    stack.append(i)

print(fear%mod)