#!/usr/bin/python3

# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following specifications:

# - Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# - The design should have 'WELCOME' written in the center.
# - The design pattern should only use ["|",".","-"] characters.

size = input().split()
width = int(size[1])
height = int(size[0])

decore = ".|."
x = 1

for i in range(1, int(height/2)+1):
    newdecor = decore * x
    print(newdecor.center(width,'-'))
    x += 2

print('WELCOME'.center(width,'-'))

for i in range(int(height/2), 0, -1):
    x -= 2
    newdecor = decore * x
    print(newdecor.center(width,'-'))

