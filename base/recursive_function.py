#!/usr/bin/python3

print("### Factorial Using Recursion ###")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
N = int(input())
print(factorial(N))

print("### Palindromic ###")
def palindromic(n):
    if n <= 1:
        return 1
    else:
        return palindromic(n-1)*10 + n

print("### Recursive ###")
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n//10, rev*10 + n % 10)

import math

def count_digits(n):
    if n == 0:
        return 1  # Special case for 0
    return math.floor(math.log10(abs(n))) + 1


N = int(input())

print(1)
for i in range(2,N+1):
    m = 10 ** (i-1)
    print(palindromic(i)*m + reverse_number(palindromic(i-1)))








