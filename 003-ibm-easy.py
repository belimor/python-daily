#!/usr/bin/python3

# This problem was asked by IBM.
# Given an integer, find the next permutation of it in absolute order.
# For example, given 48975, the next permutation would be 49578.

def next_permutation_number(num):
    digits = list(str(num))
    n = len(digits)

    i = n -2 
    while i >=0 and digits[i] > digits[i+1]:
        i -= 1

    if i < 0:
        return int(''.join(sorted(digits)))

    j = n - 1
    while digits[i] <= digits[j]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits = digits[:i + 1] + digits[i + 1:][::-1]

    return int(''.join(digits))

print("48975", next_permutation_number(48975), "Expected Output: 49578")
print("12345", next_permutation_number(12345), "Expected Output: 12354")
print("54321", next_permutation_number(54321), "Expected Output: 12345")
print("53421", next_permutation_number(53421), "Expected Output: 54123")  

