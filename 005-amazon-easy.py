#!/usr/bin/python3

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters 
# as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits 
# and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

def encode_string(my_string):
    i = 1
    count = 1
    code = ""

    while i < len(my_string):
        if my_string[i] == my_string[i-1]:
            count += 1
        else:
            code = code + str(count) + my_string[i-1]
            count = 1
        i += 1
    code = code + str(count) + my_string[i-1]
    return code

def decode_string(code):
    decode = ""
    i = 0

    while i < len(code):
        decode = decode + str(int(code[i]) * code[i+1])
        i += 2
    return decode

encode = encode_string("AAAABBBCCDAA")
print(encode)
print(decode_string(encode))



