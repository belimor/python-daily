#!/usr/bin/python3

# You are given a spreadsheet that contains a list of N athletes 
# and their details (such as age, height, weight and so on). 
# You are required to sort the data based on the K-th attribute 
# and print the final resulting table. 
# Follow the example given below for better understanding.

# image

# Note that K is indexed from 0 to M-1, where M is the number of attributes.

# Note: If two attributes are the same for different rows, for example, 
# if two atheletes are of the same age, print the row that appeared first in the input.

# Input Format

# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.

# Constraints

# Output Format

# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

# Sample Input 0
mline = """
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
"""
print(mline)
# Explanation 0

# The details are sorted based on the second attribute, since K is zero-indexed.

# data = []
# N,M = list(map(int, input().split()))
# for x in range(N):
#     data.append(list(map(int, input().split())))
# K = int(input())
# sorted_data = sorted(data, key = lambda x: x[K])
# for z in sorted_data:
#     rstr = ""
#     for y in z:
#         rstr = rstr + str(y) + " "
#     print(rstr.rstrip())

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())

    sorted_data = sorted(arr, key = lambda x: x[k])
    for z in sorted_data:
        rstr = ""
        for y in z:
            rstr = rstr + str(y) + " "
        print(rstr.rstrip())


