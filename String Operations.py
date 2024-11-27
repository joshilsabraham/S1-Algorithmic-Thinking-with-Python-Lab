'''
Author: Joshil S Abraham
Date: 19/11/2024
Description: Program to create two separate strings containing your first and  last name.
             Concatenate the two strings with a space in between and store the result in a new variable.
             From the concatenated string, accessing and printing a sub-string that consists of the last name only.
'''
first_name = (input("Enter your first name:"))
last_name = (input("Enter your last name:"))
name = (first_name + " " + last_name)
print(name)
length = len(name)
print(f"The number of characters in name is {length}")
first_name_length = len(first_name)
extracted_string = name[length:]
print(extracted_string1)
