'''
Author: Joshil S Abraham
Date: 28/10/2024
Description: Program to check whether the given number is a valid mobile number or not using functions.
             Condition for Validity:
                 Every number should contain exactly 10 digits.
                 The first digit should be 7 or 8 or 9
'''
def check_validity(phone_number):
    if len(phone_number) == 10 and phone_number[0] in "789":
        print("Valid")
    else:
        print("Invalid")
check_validity("98183773993")
