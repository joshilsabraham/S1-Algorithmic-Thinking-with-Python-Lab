'''
Author: Joshil S Abraham
Date: 29/11/2024
Description: Recursive function to multiply two positive numbers
'''
def recursive_multiplication(num_1,num_2):
    if num_1==0 or num_2 ==0:
        return 0
    else:
        return num_1+recursive_multiplication(num_1 , num_2-1)
num_1 = int(input("Enter a number : "))
num_2 = int(input("Enter second number: "))
if (num_1>0) and (num_2>0):
    result = recursive_multiplication(num_1,num_2)
    print(f"The multiplication of {num_1} and {num_2} is {result}")
else:
    print("The given numbers are not positive numbers")
