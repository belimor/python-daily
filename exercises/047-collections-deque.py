#!/usr/bin/python3

# collections.deque()

# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

# Example

# Code

# >>> from collections import deque
# >>> d = deque()
# >>> d.append(1)
# >>> print d
# deque([1])
# >>> d.appendleft(2)
# >>> print d
# deque([2, 1])
# >>> d.clear()
# >>> print d
# deque([])
# >>> d.extend('1')
# >>> print d
# deque(['1'])
# >>> d.extendleft('234')
# >>> print d
# deque(['4', '3', '2', '1'])
# >>> d.count('1')
# 1
# >>> d.pop()
# '1'
# >>> print d
# deque(['4', '3', '2'])
# >>> d.popleft()
# '4'
# >>> print d
# deque(['3', '2'])
# >>> d.extend('7896')
# >>> print d
# deque(['3', '2', '7', '8', '9', '6'])
# >>> d.remove('2')
# >>> print d
# deque(['3', '7', '8', '9', '6'])
# >>> d.reverse()
# >>> print d
# deque(['6', '9', '8', '7', '3'])
# >>> d.rotate(3)
# >>> print d
# deque(['8', '7', '3', '6', '9'])

# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format

# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Output Format

# Print the space separated elements of deque d.

# Sample Input
mline = """
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2
"""
print(mline)
from collections import deque

d = deque()
N = int(input())
for i in range(N):
    commands = []
    commands = input().split()
    if commands[0] == "append":
        d.append(int(commands[1]))
    elif commands[0] == "appendleft":
        d.appendleft(int(commands[1]))
    elif commands[0] == "pop":
        d.pop()
    elif commands[0] == "popleft":
        d.popleft()
    else:
        print("Error")

result = ""
for i in d:
    result = result + str(i) + " "

print(result.strip())




