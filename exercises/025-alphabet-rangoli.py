#!/usr/bin/python3

# You are given an integer, n. 
# Your task is to print an alphabet rangoli of size n. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----
import string

def print_rangoli(size):
    # your code goes here
    letters = string.ascii_lowercase[:size]
    width = (size-1)*4+1
    dcenter = ""
    x = 1
    while x < size:
        mcenter = dcenter[0:len(dcenter)+1] + letters[size-x] + dcenter[::-1]
        print(mcenter.center(width,"-"))
        dcenter = dcenter + letters[size-x] + "-"
        x += 1
    mcenter = dcenter[0:len(dcenter)+1] + letters[size-x] + dcenter[::-1]
    print(mcenter.center(width,"-"))
    x = size-1
    while x > 0:
        dcenter = dcenter[0:len(dcenter)-2]
        mcenter = dcenter[0:len(dcenter)+1] + letters[size-x] + dcenter[::-1]
        print(mcenter.center(width,"-"))
        x -= 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
