#!/usr/bin/python3

# Integers (int)

x = 10
y = -50
z = 0

print("x:",x,"Type:",type(x))
print("y:",y,"Type:",type(y))
print("z:",z,"Type:",type(z))

# Floating-Point Numbers (float)

a = 3.14
b = -0.0001
c = 1.2e3 # 1.2 x 10^3 = 1200.0

print("a:",a,"Type:",type(a))
print("b:",b,"Type:",type(b))
print("c:",c,"Type:",type(c))

# Complex Numbers (complex)

p = 2 + 3j
q = -5j
r = 7

print("p:",p,"Type:",type(p))
print("q:",q,"Type:",type(q))
print("Real part of p:",p.real)
print("Imaginary part of p:",p.imag)

# Numeric Operations

x = 10
y = 3
print(x,y)
print("Addition (x+y):", x + y)
print("Substruction (x-y):", x - y)
print("Multiplication (x*y):", x * y)
print("Division (x/y):", x / y)
print("Subdivision (x//y):", x // y)
print("Modulus (x%y):", x % y)
print("Exponentiation (x**y):", x ** y)

# Type Conversion

x = 5
y = float(x)
z = int(3.14)
print(y)
print(z)

# Math Functions

import math

x = -10
y = 9.7

print(abs(x))
print(math.sqrt(y))
print(pow(2,3))
print(math.floor(y))
print(math.ceil(y))

# The function pow(x, y, z) computes x^y mod z, which means it calculates the result of x raised to the power of y, then takes the remainder when divided by z.
print(pow(3,2,5))
print(9/5)

# round
num = 3.14159265359
limited_num = round(num, 2)
print(limited_num)

# formatted number
num = 3.14159265359
formatted_num = f"{num:.2f}"  # Format to 2 decimal places
print(formatted_num)  # Output: 3.14 (as a string)

