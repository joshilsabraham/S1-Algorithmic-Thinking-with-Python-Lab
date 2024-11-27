'''
Author: Joshil S Abraham
Date: 19/10/2024
Description: Program that performs the following tasks:
             User Input, Addition, Subtraction, Multiplication, 
             Division, Modulus and Combined Arithmetic Operation

'''
# User Input
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
num3=int(input("Enter the Third Number:"))
# Addition
print(f"The Sum of {num1} and {num2} is {num1+num2}")
# Subtraction
print(f"The Difference when {num2} is subtracted from {num1} is {num2-num1}")
# Multiplication
print(f"The Product of {num1} and {num2} is {num1*num2}")
# Division
print(f"The Quotient when {num1} is divided by {num2} is {num1/num2}")
# Modulus
print(f"The Remainder when {num1} is divided by {num2} is {num1%num2}")
# Combined Arithmetic Operation:
print(f"The Result of ({num1} + {num2}) * {num3} / 2 is {(num1+num2)*num3/2}")
