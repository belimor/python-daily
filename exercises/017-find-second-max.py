#!/usr/bin/python3

# Hackerrank:
# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given n scores. 
# Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. 
# The second line contains an array A[] of n integers each separated by a space.

# Example:
# 5
# 2 3 6 6 5
# Result:
# 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
        
    my_list = list(sorted(set(arr)))
    print(my_list[-2])
