#!/usr/bin/python3

# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0-9).
# It should only contain alphanumeric characters ( a-z ,  A-Z  &  0-9 ).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

# Input Format

# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.

# Output Format

# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

# Sample Input
mline = """
2
B1CD102354
B1CDEF2354
Sample Output
Invalid
Valid
"""
print(mline)

# Explanation
# B1CD102354: 1 is repeating → Invalid
# B1CDEF2354: Valid

T = int(input())
results = []
for i in range(T):
    uid = input()
    #uid = s
    # It must contain at least 2 uppercase English alphabet characters.
    upper_count = 0
    upper_check = False
    # It must contain at least 3 digits (0-9).
    digi_count = 0
    digi_check = False
    # It should only contain alphanumeric characters ( a-z ,  A-Z  &  0-9 ).
    alphanumeric_check = True
    for c in uid:
        if c.isupper():
            upper_count += 1
        if c.isdigit():
            digi_count += 1
        if not c.isalnum():
            alphanumeric_check = False
    if upper_count > 1:
        upper_check = True
    if digi_count > 2:
        digi_check = True
    # No character should repeat.
    set_uid = set(uid)
    repeat_check = True
    if len(set_uid) < len(uid):
        repeat_check = False
    # There must be exactly 10 characters in a valid UID.
    len_check = False
    if len(uid) == 10:
        len_check = True
    final_check = len_check and repeat_check and digi_check and upper_check and alphanumeric_check
    if final_check == True:
        results.append("Valid")
    else:
        results.append("Invalid")
for r in results:
    print(r)


