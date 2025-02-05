#!/usr/bin/python3

# Consider the following:
# - A string, S, of length n where S = c(0)c(1)...c(n-1).
# - An integer, k, where k is a factor of n.

# We can split S into n/k substrings where each subtring, t(i), consists of a contiguous block of k characters in S. 
# Then, use each t(i) to create string u(i) such that:
# - The characters in u(i) are a subsequence of the characters in t(i).
# - Any repeat occurrence of a character is removed from the string such that each character in u(i) occurs exactly once. In other words, if the character at some index j in t(i) occurs at a previous index <j in t(i), then do not include the character in string u(i).

# Given S and k, print n/k lines where each line i denotes string u(i).

# Example

# S = 'AAABCADDE'
# k = 3

# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u(1) = 'A'. The second substring has all distinct characters, so u(2) = 'BCA'. The third substring has 2 different characters, so u(3) = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

# Function Description

# Complete the merge_the_tools function in the editor below.
# merge_the_tools has the following parameters:
# - string s: the string to analyze
# - int k: the size of substrings to analyze

# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Sample Input

# AABCAAADA
# 3

# Sample Output

# AB
# CA
# AD

def merge_the_tools(string, k):
    # your code goes here
    substrings = []
    for i in range(0,len(string)+1-k,k):
        substrings.append(string[i:k+i])
    for u in substrings:
        subsequence = ""
        for char in u:
            if char not in subsequence:
                subsequence = subsequence + char
        print(subsequence)
    print(substrings)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)











