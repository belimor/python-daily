#!/usr/bin/python3

# This problem was asked by Atlassian.
#
# MegaCorp wants to give bonuses to its employees 
# based on how many lines of codes they have written. 
# They would like to give the smallest positive amount to each worker 
# consistent with the constraint that 
# if a developer has written more lines of code than their neighbor, 
# they should receive more money.
#
# Given an array representing a line of seats of employees at MegaCorp, 
# determine how much each one should get paid.
#
# For example, given [10, 40, 200, 1000, 60, 30], 
# you should return [1, 2, 3, 4, 2, 1].

def calculate_bonuses(lines_of_code):
    n = len(lines_of_code)
    bonuses = [1] * n # Initialize all bonuses to 1

    for i in range(1,n):
        if lines_of_code[i] > lines_of_code[i-1]:
            bonuses[i] = bonuses[i-1] + 1

    for i in range(n-2,-1,-1):
        if lines_of_code[i] > lines_of_code[i+1]:
            bonuses[i] = max(bonuses[i], bonuses[i+1] + 1)

    return(bonuses)

lines_of_code = [10, 40, 200, 1000, 60, 30]
print(calculate_bonuses(lines_of_code))
lines_of_code = [10, 40, 200, 1000, 60, 70]
print(calculate_bonuses(lines_of_code))




