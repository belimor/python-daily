#!/usr/bin/python3

# The textwrap module in Python is used to format and manipulate plain text 
# by wrapping and indenting it to fit specific widths. 

import textwrap

# Basic Wrapping with textwrap.wrap()

text = "Python is an amazing programming language. It is versatile and easy to learn."
wrapped_text = textwrap.wrap(text, width=30)

print(wrapped_text)
