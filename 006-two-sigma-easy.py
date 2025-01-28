#!/usr/bin/python3

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).

import random

def rand7():
    return random.randint(1,7)

print(rand7())

def rand5():
    n = 6
    while n > 5:
        n = rand7()
        print("n:",n)
    return n

print(rand5())

def rand52():
    while True:
        num = rand7()
        print("num:",num)
        if num <= 5:
            return num

print(rand52())
