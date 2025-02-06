#!/usr/bin/python3

# dot

# The dot tool returns the dot product of two arrays.

# import numpy

# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.dot(A, B)       #Output : 11

# cross

# The cross tool returns the cross product of two arrays.

# import numpy

# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.cross(A, B)     #Output : -2

# Task

# You are given two arrays A and B. Both have dimensions of N x N.
# Your task is to compute their matrix product.

# Input Format

# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.

# Output Format

# Print the matrix multiplication of A and B.

# Sample Input

# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output

# [[ 7 10]
#  [15 22]]

import numpy

my_list1 = []
my_list2 = []

N = input()
for i in range(int(N)):
    x = list(map(int, input().split()))
    my_list1.append(x)

for i in range(int(N)):
    x = list(map(int, input().split()))
    my_list2.append(x)

A = numpy.array(my_list1)
B = numpy.array(my_list2)

result = numpy.dot(A, B)
print(result)


