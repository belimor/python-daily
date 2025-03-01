#!/usr/bin/python3

# ABC is a right triangle, 90 degree at B.
# Therefore, angel ABC = 90 degree.

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find angel MBC (angle X degree, as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# Lengths AB and BC are natural numbers.

# Output Format

# Output angel MBC in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.

# Sample Input
mline = """
10
10
Sample Output
45°
"""
print(mline)

import math

AB = int(input())
BC = int(input())

def median_angle(b,a):
    theta = math.degrees(math.atan(b/a)) # 
    return theta

theta = median_angle(AB, BC)
#print(f"Median angle (θ) = {theta:.2f}°")
print(f"{theta:.0f}{chr(176)}")



