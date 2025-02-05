#!/usr/bin/python3

# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

import re

def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    players = {"Stuart": 0,"Kevin": 0}
    scounted = []
    kcounted = []
    str_len = len(string)
    
    i = 0
    for i in range(str_len+1):
        for slen in range(i+1, str_len+1):
            if string[i:i+1] in vowels:
                if string[i:slen] not in kcounted:
                    pattern = f"(?={re.escape(string[i:slen])})"
                    players['Kevin'] = players['Kevin'] + len(re.findall(pattern, string)) #string.count(string[i:slen])
                    kcounted.append(string[i:slen])
            else: 
                if string[i:slen] not in scounted:
                    pattern = f"(?={re.escape(string[i:slen])})"
                    players['Stuart'] = players['Stuart'] + len(re.findall(pattern, string)) ##string.count(string[i:slen])
                    scounted.append(string[i:slen])

    if players['Stuart'] > players['Kevin']:
        return print("Stuart", players['Stuart'])
    elif players['Stuart'] < players['Kevin']:
        return print("Kevin", players['Kevin'])
    else:
        return print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)




