#!/usr/bin/python3

# map() function applies a given function to all items in an iterable (like a list or tuple) 
# and returns a map object, which is an iterator. 
# You can then convert the result to a list, tuple, or other collection.

# map(function, iterable, ...)

# Basic Example
def square(x):
    return x ** 2

numbers = [1,2,3,4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

# Using Lambda with map()
numbers = [1,2,3,4]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

# Mapping Multiple Iterables
num1 = [2,4,6]
num2 = [3,5,7]
sum_num = map(lambda x,y: x+y, num1, num2)
print(list(sum_num))

# Using Built-in Functions
words = ["hello","world","python"]
upper_words = map(str.upper, words)
print(list(upper_words))

# Filtering with map()
numbers = [1,2,3,4,5,6,7]
even_numbers = filter(lambda x: x%2 == 0, numbers)
is_even = list(map(lambda x: x%2 == 0, numbers))
print(numbers)
print(list(is_even))
print(list(even_numbers))

# Converting map() Output to Other Types
numbers = [1,2,3,4,5,6,7]
squared_numbers = map(lambda x: x**2, numbers)
print(tuple(squared_numbers))
#squared_numbers = map(lambda x: x**2, numbers)
print(set(squared_numbers))

# Custom Object with map()
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return(f"Hello, {self.name}!")

people = [Person("Alice"), Person("John"), Person("Bob")]
greetings = map(lambda person: person.greet(), people)
print(list(greetings))





