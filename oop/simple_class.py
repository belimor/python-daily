#!/usr/bin/python3


class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to update age
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Create the instance of the class
person1 = Person("Alice", 17)

# Call methods on the object
person1.display_info()
person1.have_birthday()
person1.display_info()


