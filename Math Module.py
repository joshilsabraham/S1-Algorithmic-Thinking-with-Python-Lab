'''
Author: Joshil S Abraham
Date: 18 / 10 / 2024
Description: Program to find the square root, calculate the factorial and raise the number 
             to the power of 2 using functions from the math module
'''
import math    # Importing math module
number = int(input("Enter a number:"))
square_root = math.sqrt(number)    # Calculating the square root of the number
print(f"Square root of {number}: {square_root}")
factorial = math.factorial(number)    # Calculating the factorial of the number
print(f"Factorial of {number}: {factorial}")
exponentiation = math.pow(number,2)    # Raising the number to the power of 2
print(number,"raised to power 2: ",exponentiation)
