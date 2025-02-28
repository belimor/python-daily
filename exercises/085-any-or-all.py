#!/usr/bin/python3

# any()

# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.

# Code

# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False
# all()

# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

# Code

# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False

# Task

# You are given a space separated list of integers. 
# list_of_int = [1, 245, 15, 7, 55]
# If all the integers are positive, 
# is_positive = lambda p: p >= 0
# then you need to check if any integer is a palindromic integer.
# is_palindrome = lambda n: str(n) == str(n)[::-1]

# Input Format
# The first line contains an integer N. N is the total number of integers in the list.
# N = int(input().split())
# The second line contains the space separated list of  integers.
# list_of_int = list(map(int,input().split()))
# for n in list_of_int:
#     is_positive = lambda n: n >= 0
#     is_palindrome = lambda n: str(n) == str(n)[::-1]
#     all(is_positive)


# Constraints

# Output Format

# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

# Sample Input
mline = """
5
12 9 61 5 14 
Sample Output
True
"""
print(mline)

# Explanation

# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

# Hence, the output is True.

# Can you solve this challenge in 3 lines of code or less?
# There is no penalty for solutions that are correct but have more than 3 lines.

N = int(input())
list_of_int = list(map(int,input().split()))
print(all(list(map(lambda p: p >= 0, list_of_int))) and any(list(map(lambda n: str(n) == str(n)[::-1], list_of_int))))




