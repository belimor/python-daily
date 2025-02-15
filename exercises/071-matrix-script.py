#!/usr/bin/python3

# Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space ' ' for better readability.

# Neo feels that there is no need to use 'if' conditions for decoding.

# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

# Input Format

# The first line contains space-separated integers N (rows) and M (columns) respectively.
# The next N lines contain the row elements of the matrix script.

# Constraints
# 0 < N,M < 100

# Note: A 0 score will be awarded for using 'if' conditions in your code.

# Output Format

# Print the decoded matrix script.

# Sample Input 0
mline = """
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Sample Output 0
This is Matrix#  %!
"""
print(mline)

# Explanation 0
# The decoded script is:
# This$#is% Matrix#  %!
# Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.
# So, the final decoded script is:
# This is Matrix#  %!
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
my_matrix = []
for z in range(m):
    my_matrix.append('')
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    for c in range(m):
        my_matrix[c] = my_matrix[c] + matrix_item[c]
matrix_line = ""
for q in my_matrix:
    matrix_line += q
i = 0
while i < len(matrix_line) and not matrix_line[i].isalnum():
    i += 1
p0 = matrix_line[:i]
tmp_str = matrix_line[i:]
i = len(tmp_str)-1
while i > 0 and not tmp_str[i].isalnum():
    i -= 1
p1 = tmp_str[:i+1]
p2 = tmp_str[i+1:]
p1_cleaned = re.sub(r'[^a-zA-Z0-9]', ' ', p1)
p1_double_cleaned = re.sub(r'\s+', ' ', p1_cleaned).strip()
print(p0 + p1_double_cleaned + p2)

