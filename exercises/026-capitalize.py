#!/usr/bin/python3

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.


# Complete the solve function below.
def solve(s):
    string = s
    new_string = ""
    priv_char = ""
    i = 0
    for char in string:
        if priv_char == " " or priv_char == "":
            new_string = new_string + char.capitalize()
        else:
            new_string = new_string + char
        priv_char = char
        i += 1
    print(new_string)

    return new_string


if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)

