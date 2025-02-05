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
import time

def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    str_len = len(string)

    # Scores for Stuart (consonants) and Kevin (vowels)
    stuart_score = 0
    kevin_score = 0

    # Iterate through the string
    for i in range(str_len):
        # Score is the number of substrings starting from this position
        score = str_len - i
        if string[i] in vowels:
            kevin_score += score
        else:
            stuart_score += score

    # Determine the winner
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()

    start_time = time.time()
    result = sum(range(1_000_000))

    minion_game(s)

    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")




