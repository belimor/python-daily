#!/usr/bin/python3

# You are given a string S.
# S contains alphanumeric characters only.

# Your task is to sort the string S in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format
# A single line of input contains the string S.

# Constraints

# Output Format
# Output the sorted string S.

# Sample Input
mline = """
Sorting1234
Sample Output
ginortS1324
"""
print(mline)

S = input()
low_let = []
upper_let = []
odd_digits = []
even_digits = []

for c in S:
    if c.islower():
        low_let.append(c)
    elif c.isupper():
        upper_let.append(c)
    else:
        if int(c)%2 == 0:
            even_digits.append(c)
        else:
            odd_digits.append(c)
result = ''.join(sorted(low_let)) + ''.join(sorted(upper_let)) + ''.join(sorted(odd_digits)) + ''.join(sorted(even_digits))
print(result)


