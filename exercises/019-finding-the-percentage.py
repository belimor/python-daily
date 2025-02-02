#!/usr/bin/python3

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example
# marks key:value pairs are:
#     'alpha':[20,30,40]
#     'beta':[30,50,70]
# The query_name is 'beta'. 
# beta's average score is (30+50+70)/3.

# Input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Output:
# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = 0
    sum = 0
    for score in student_marks[query_name]:
        sum += score 
        x += 1
        print(score)
    print(sum)
    average = sum/x
    print(f"{average:.2f}")



















