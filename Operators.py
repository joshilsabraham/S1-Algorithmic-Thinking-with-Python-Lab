'''
Author: Joshil S Abraham
Date: 18/10/2024
Description: Program that demonstrates the usage of arithmetic, comparison, and logical operators. 
'''
number_1 = int(input("Enter First Number:"))
number_2 = int(input("Enter Second Number:"))
addition = number_1 + number_2    # Addition
if number_1 > number_2:
  difference = number_1 - number_2    # Subtraction
else:
  difference = number_2 - number_1
product = number_1 * number_2    # Multiplication
quotient = number_1 / number_2    # Division
print(f"Sum: {addition}, Difference: {difference}, Product: {product}, Quotient:{quotient}")
comparison = number_1 > number_2    # Comparing both numbers
print("Is a greater than b?")
if comparison == True:
  print("Yes")
else:
  print("No")
equality = number_1 == number_2    # Checking if both numbers are equal
print("Are a and b equal?")
if equality == True:
  print("Yes")
else:
  print("No")
logical_and = number_1 > 0 and number_2 > 0    # Logical Operations
logical_or = number_1 < 0 or number_2 < 0
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
