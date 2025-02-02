#!/usr/bin/python3

# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

# Sample Input:
# qA2

# Sample Output:
# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    alphanumeric = alphabeticala = digits = lowercase = uppercase = False
    for char in s:
        alphanumeric = alphanumeric or char.isalnum()
        alphabeticala = alphabeticala or char.isalpha()
        digits = digits or char.isdigit()
        lowercase = lowercase or char.islower()
        uppercase = uppercase or char.isupper()
    print(alphanumeric)
    print(alphabeticala)
    print(digits)
    print(lowercase)
    print(uppercase)


