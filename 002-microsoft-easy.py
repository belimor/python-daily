#!/usr/bin/python3

# This problem was asked by Microsoft.
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

def nth_perfect_number(n):
    msum = sum(int(x) for x in str(n))
    if msum <= 10:
        nn = 10 - msum
        pn = str(n) + str (nn)
        return(int(pn))
    else:
        pn = "The sum of the digits has already exceeded 10."
        return(pn)

print(nth_perfect_number(1))
print(nth_perfect_number(9))
print(nth_perfect_number(10))
print(nth_perfect_number(11))
print(nth_perfect_number(33))
print(nth_perfect_number(333))
print(nth_perfect_number(3333))

