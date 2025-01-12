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


