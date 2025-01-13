#!/usr/bin/python3

class test:
    def __init__(self, b1="DoSelect"):
        self.B1 = b1
        b1 = "dOsELECT"  # This line does not affect self.B1

    def display(self):
        print(self.B1)

object1 = test()
object1.display()

