'''
Author: Joshil S Abraham
Date: 29/11/2024
Description: Recursive function to add two positive numbers.
'''
def recursive_addition(num_1,num_2):
    if num_2 == 0:
        return num_1
    else:
        return recursive_addition(num_1+1, num_2-1)
num_1=int(input("Enter a Number:"))
num_2=int(input("Enter a Number:"))
if (num_1>0) and (num_2>0):
  sum=recursive_addition(num_1,num_2)
  print(f"The Sum of {num_1} and {num_2} is {sum}")  
else:
  print("The given numbers are not positive numbers")
