#!/usr/bin/python3

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# - string string: a long string
# - int max_width: the width to wrap to

# Returns
# string: a single string with newline characters ('\n') where the breaks should be

import textwrap

def wrap(string, max_width):
    wrapped_string = textwrap.wrap(string,width=max_width)
    result = ("\n".join(wrapped_string))
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
