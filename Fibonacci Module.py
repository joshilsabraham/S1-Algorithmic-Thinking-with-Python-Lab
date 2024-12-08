'''
Author: Joshil S Abraham
Date: 28/10/2024
Description: Program to define a module to find Fibonacci Numbers and 
             import the module to another program
'''
#fibonacci.py
def fibonacci_number(num):
    lst=[0]
    num1=0
    num2=1
    for i in range(num-1):
        lst.append(num2)
        num1,num2=num2,num1+num2
    return lst

#fibonacci_module.py
from fibonocci import fibonacci_number
num=int(input("Enter a number:"))
print(fibonacci_number(num))
