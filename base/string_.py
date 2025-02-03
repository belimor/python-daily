#!/usr/bin/python3

string1 = 'Hello'
string2 = "WorlD"
mlstring = '''
test1
test2
test3
'''

# Accessing Characters in Strings. Slicing Strings.
print(string1[0])
print(string2[-1])
print(string1[:4])
print(string2[:])

# String Methods
string3 = string1 + " " + string2
print(string3.upper())
print(string3.lower())
print(string3.capitalize())
print(string3.title())

# Trimming and Padding
string = "   Hello World   "
print(f"==={string}===")
print(f"==={string.strip()}===")
print(f"==={string.lstrip()}===")
print(f"==={string.rstrip()}===")

# Finding and replacing
print(string.find("Hello"))
print(string.replace("Hello", "Python"))

# Checking Conditions
text="hello123"
print("===================")
print(text)
print(f"Check if all characters are alphabetic: {text.isalpha()}")
print(f"Check if all characters are numeric: {text.isdigit()}")
print(f"Check if all characters are alphanumeric: {text.isalnum()}")
print("Check if string starts with a specific substring: " + str(text.startswith('hello')))
print("Check if string ends with a specific substring: " + str(text.endswith("123")))

# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# String Iteration
text = "Python"
for c in text:
    print(c)

# String Formatting
# Old style
print("Hello, %s" % "Alice")
# str.format()
print("Hello, {}".format("Bob"))
# f-strings (Python 3.6+)
name = "John"
print(f"Hello, {name}")

# Splitting and Joining
text = "apple,banana,orange"
print(text)
fruits = text.split(",")
print(fruits)
newtext = " | ".join(fruits)
print(newtext)

# Use a backslash (\) to include special characters
text = "\"Python\""
print(text)

# Raw Strings
text = r"C:\DIR"
print(text)

# String Comparison
str1 = "python"
str2 = "Python"
print(str1 == str2)
print(str1.lower() == str2.lower())




