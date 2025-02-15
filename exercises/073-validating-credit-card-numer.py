#!/usr/bin/python3

# You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

# A valid credit card from ABCD Bank has the following characteristics:

#► It must start with a 4, 5 or 6.
#► It must contain exactly 16 digits.
#► It must only consist of digits (0-9).
#► It may have digits in groups of 4, separated by one hyphen "-".
#► It must NOT use any other separator like ' ' , '_', etc.
#► It must NOT have 4 or more consecutive repeated digits.

# Examples:

# Valid Credit Card Numbers

# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214

# Invalid Credit Card Numbers

# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

# Input Format

# The first line of input contains an integer N.
# The next N lines contain credit card numbers.

# Constraints
# 0 < N < 100

# Output Format

# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

# Sample Input
mline1 = """
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
# Sample Output =====================
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid
"""
mline = """
5
7165863385679329
6175824393389297
5252248277877418
9563584181869815
5179123424576876
====
Invalid
Valid
Valid
Invalid
Valid
"""
print(mline)

# Explanation
# 4123456789123456 : Valid
# 5123-4567-8912-3456 : Valid
# 61234--8912-3456 : Invalid, because the card number is not divided into equal groups of .
# 4123356789123456 : Valid
# 51-67-8912-3456 : Invalid, consecutive digits  is repeating  times.
# 5123456789123456 : Invalid, because space '  ' and - are used as separators.

N = int(input())
results = []
for i in range(N):
    card = input()

    # It must start with a 4, 5 or 6
    start_check = False
    if card[0] in ['4','5','6']:
        start_check = True

    # It must NOT use any other separator like ' ' , '_', etc.
    # It must only consist of digits (0-9)
    digit_check = True
    # It must contain exactly 16 digits.
    digit_count = 0
    x16d_check = False
    # It may have digits in groups of 4, separated by one hyphen "-".
    x4g_count = 0
    x4g_check = True
    # It must NOT have 4 or more consecutive repeated digits.
    x4consec_count = 1
    last_c = ""
    x4consec_check = True
    for c in card:
        if not c.isdigit():
            if c != "-":
                digit_check = False
        if c.isdigit():
            digit_count += 1
        if c.isdigit():
            x4g_count += 1
        if c == "-" and x4g_count != 4:
            x4g_check = False
        if c == "-" and x4g_count == 4:
            x4g_count = 0

        if c.isdigit() and c == last_c:
            x4consec_count += 1
            if x4consec_count >= 4:
                x4consec_check = False
        if c.isdigit() and c != last_c:
            x4consec_count = 1
        if c.isdigit():
            last_c = c
        #print("c:",c,"last_c:",last_c,"x4consec_count:", x4consec_count)

    if digit_count == 16:
        x16d_check = True
    final_check = x16d_check and x4consec_check and x4g_check and digit_check and start_check
    #print("x16d_check:", x16d_check, "x4consec_check:", x4consec_check, "x4g_check:", x4g_check, "digit_check:", digit_check, "start_check:", start_check)
    if final_check:
        results.append("Valid")
    else:
        results.append("Invalid")
    #print(final_check)
for chk in results:
    print(chk)



