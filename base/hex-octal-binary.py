#!/usr/bin/python3

# Conversions between Decimal, Octal, Hexadecimal, and Binary

decimal_number = int(input("Enter your number: "))

# Convert to other bases:
octal_number = oct(decimal_number)
hexadecimal_number = hex(decimal_number).upper()
binary_number = bin(decimal_number)

# Format outputs (removing prefix):
formatted_octal = octal_number[2:]
formatted_hexadecinal = hexadecimal_number[2:]
formatted_binary = binary_number[2:]

print("Octal Number:", formatted_octal)
print("Hexadecimal Number", formatted_hexadecinal)
print("Binary Number", formatted_binary)
