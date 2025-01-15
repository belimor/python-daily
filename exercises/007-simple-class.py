#!/usr/bin/python3

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods. 

class InputOutputString():
    def __init__(self):
        self.s=""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

def test_InputOutputString():
    print("Testing InputOutputString class:")
    strobj = InputOutputString()
    strobj.getString()
    print("String in uppercase:")
    strobj.printString()

test_InputOutputString()

