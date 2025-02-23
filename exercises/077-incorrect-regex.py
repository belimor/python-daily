#!/usr/bin/python3

# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format

# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.

# Constraints
# 0 < T < 100

# Output Format

# Print "True" or "False" for each test case without quotes.

# Sample Input
mline = """
2
.*\+
.*+
Sample Output
True
False
"""
print(mline)

# Explanation
# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

import re

T = int(input())
results = []
for x in range(T):
    string = input()
    try:
        re.compile(string)
        results.append(True)
    except re.error:
        results.append(False)
for x in results:
    print(x)






