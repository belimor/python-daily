#!/usr/bin/python3

# Given an integer, n, print the following values for each integer i from 1 to n:
# - Decimal
# - Octal
# - Hexadecimal (capitalized)
# - Binary

# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print
# prints

# The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n and the values should be separated by a single space.

def print_formatted(number):
    # your code goes here
    last_binary_number = bin(n)
    width = len(last_binary_number[2:])
    for i in range(1,n+1):

        decimal_number = i
        octal_number = oct(i)
        hexadecimal_number = hex(i).upper()
        binary_number = bin(i)

        octal_cleaned = octal_number[2:]
        hexadecimal_cleaned = hexadecimal_number[2:]
        binary_cleaned = binary_number[2:]

        formatted_number = str(decimal_number).rjust(width)
        formatted_octal = octal_cleaned.rjust(width)
        formatted_hexadecimal = hexadecimal_cleaned.rjust(width)
        formatted_binary = binary_cleaned.rjust(width)

        print(f"{formatted_number} {formatted_octal} {formatted_hexadecimal} {formatted_binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
