'''
Author: Joshil S Abraham
Date: 18 / 10 / 2024
Description: Program that demonstrates the usage of arithmetic,
             comparison, and logical operators. Perform a few
             operations and print the results.
'''
number_1=int(input("Enter First Number:"))
number_2=int(input("Enter Second Number:"))
addition=number_1+number_2
division=number_1/number_2
print("Sum:",addition,"Division:",division)
comparison=number_1>number_2
print("Is a greater than b?:",comparison)
equality=number_1==number_2
print("Are a and b equal?",equality)
logical_and=number_1>0 and number_2>0
logical_or=number_1<0 or number_2<0
print("Logical AND:",logical_and)
print("Logical OR:", logical_or)
