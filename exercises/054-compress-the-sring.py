#!/usr/bin/python3

# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

# For a better understanding of the problem, check the explanation.

# Input Format

# A single line of input consisting of the string S.

# Output Format

# A single line of output consisting of the modified string.

# Constraints

# All the characters of S denote integers between 0 and 9.
# 1 <= S <= 10**4

# Sample Input

mline = """
# 1222311
# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)
"""
print(mline)

# Explanation

# First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

# Also, note the single space within each compression and between the compressions.

from itertools import groupby
in_str = input()
groups = []
uniquekeys = []
for k, g in groupby(in_str):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
result = ""
for i in range(len(uniquekeys)):
    result += "(" + str(len(groups[i])) + ", " + str(uniquekeys[i]) + ") "
print(result.rstrip())

