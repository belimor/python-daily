#!/usr/bin/python3

# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [["A",20.0],["C",50.0],["B",50.0]]
#
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50. 
# There are two students with that score: ["C","B"]. 
# Ordered alphabetically, the names are printed as:

# B
# C

if __name__ == '__main__':
    records = []
    scores = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    sorted_scores = list(sorted(set(scores)))
    second_lowest = sorted_scores[1]

    for student in records:
        if student[1] == second_lowest:
            result.append(student[0])

    for name in sorted(result):
        print(name)

