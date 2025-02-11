#!/usr/bin/python3

# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

# - Print the three most common characters along with their occurrence count.
# - Sort in descending order of occurrence count.
# - If the occurrence count is the same, sort the characters in alphabetical order.

# For example, according to the conditions described above,

# GOOGLE would have it's logo with the letters G, O, E.

# Input Format

# A single line of input containing the string S.

# Constraints
# 3 < len(S) <=10**4
# S has at least 3 distinct characters

# Output Format

# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0
mline = """
# aabbbccde
# Sample Output 0
# b 3
# a 2
# c 2
"""
print(mline)

# Explanation 0

# aabbbccde

# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.

logo = input()
tmp_logo = []
for c in logo:
    tmp_logo.append(c)
logo_letters = set(tmp_logo)
Max = 1
couples = []
for c in logo_letters:
    count = logo.count(c)
    if count > Max:
        Max = count
    couples.append([c,count])
result = []
for i in range(Max,0,-1):
    tmp_res = []
    for j in range(len(couples)):
        if couples[j][1] == i:
            tmp_res.append(couples[j][0])
    tmp_res.sort()
    result.append([i,tmp_res])
top = 0
for x in range(len(result)):
    for y in result[x][1]:
        print(y, result[x][0])
        top += 1
        if top >= 3:
            break
    if top >= 3:
        break


