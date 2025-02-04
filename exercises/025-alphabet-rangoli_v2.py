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
    alphabet = string.ascii_lowercase

    rows = []
    for i in range(size):
        # Get the current row letters
        left_part = "-".join(alphabet[size-1:size-i-1:-1])
        right_part = "-".join(alphabet[size-i-1:size])
        full_row = left_part + "-" + right_part if left_part else right_part

        # Center the row to match the rangoli width
        rows.append(full_row.center(4*size-3,"-"))

    # Print the rangoli
    print("\n".join(rows + rows[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
