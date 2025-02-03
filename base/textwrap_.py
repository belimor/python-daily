#!/usr/bin/python3

# The textwrap module in Python is used to format and manipulate plain text 
# by wrapping and indenting it to fit specific widths. 

import textwrap

# Basic Wrapping with textwrap.wrap()

text = "Python is an amazing programming language. It is versatile and easy to learn."
wrapped_text = textwrap.wrap(text, width=30)
print(wrapped_text)
print("\n".join(wrapped_text))

# Formatting Text with textwrap.fill()

formatted_text = textwrap.fill(text,width=30)
print(formatted_text)

# Adding Indents with textwrap.indent()

indented_text = textwrap.indent(formatted_text, prefix=">> ")
print(indented_text)

# Removing Indents with textwrap.dedent()

indented_text = """
   Python is fun.
   This text has leading spaces
"""
dedented_text = textwrap.dedent(indented_text)
print(dedented_text)

# Controlling Subsequent Line Indents with textwrap.TextWrapper

wrapper = textwrap.TextWrapper(width=30, initial_indent="==> ", subsequent_indent="    ")
formatted_text = wrapper.fill(text)
print(formatted_text)

# Shortening Text with textwrap.shorten()

short_text = textwrap.shorten(text, width=25, placeholder="...")
print(short_text)

# Customizing Wrapping Behavior

wrapper = textwrap.TextWrapper(width=20, expand_tabs=False, replace_whitespace=True)
custome_wrapped_text = wrapper.wrap("Python\tis\tawesome\tand\tfun!")
print(custome_wrapped_text)




