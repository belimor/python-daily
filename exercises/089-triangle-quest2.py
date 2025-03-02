#!/usr/bin/python3

# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321
# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# - Input Format:
# A single line of input containing the integer N.
# - Constraints:
# - Output Format:
# Print the palindromic triangle of size N as explained above.

# Sample Input
mline = """
5
Sample Output
1
121
12321
1234321
123454321
"""

N = int(input())
result = ""
x = 1
while x <= N:
    result = result + ''.join(map(str,set(range(1,x+1)))) + ''.join(map(str,set(range(x-1,0,-1)))) + '\n'
    x += 1
print(result)

# Solutin 2
N = int(input())

def palindromic(n):
    if n <= 1:
        return 1
    else:
        return palindromic(n-1)*10 + n

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n//10, rev*10 + n % 10)

print(1)
for i in range(2,N+1):
    m = 10 ** (i-1)
    print(palindromic(i)*m + reverse_number(palindromic(i-1)))


# Solution 3

for i in range(1, int(input()) + 1):
    print((10**i // 9) ** 2)


