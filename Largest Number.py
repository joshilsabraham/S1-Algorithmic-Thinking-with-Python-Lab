'''
Author: Joshil S Abraham
Date: 25 / 10 / 2024
Description: Program to find the largest of three numbers.
             The program should take three numbers as input from the user
             and determine which one is the largest.
             Use conditional statements to compare the numbers.
'''
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))
if first_number>second_number and first_number>third_number:
    print("The largest number is:",first_number)
elif second_number>first_number and second_number>third_number:
    print("The largest number is:",second_number)
elif third_number>first_number and third_number>second_number:
    print("The largest number is:",third_number)
else:
    print("Invalid")

