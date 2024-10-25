'''
Author: Joshil S Abraham
Date: 25 / 10 / 2024
Description: Program to convert temperature values back and forth
             between Celsius and Fahrenheit. The user should be able
             to input a temperature in Celsius or Fahrenheit, and the
             program should convert it to the other unit using the formula:
                               c/5=f−32/9

            For Celsius to Fahrenheit conversion:
                    f=(9/5×c)+32

            For Fahrenheit to Celsius conversion:
                    c=5/9×(f−32)
'''
temperature=float(input("Enter temperature:"))
value=input("Is this in (C)elsius or (F)ahrenheit?:")
if value=='c' or 'C':
    fahrenheit_value=(9/5*temperature)+32
    print(value, "Celsius is", fahrenheit_value,"Fahrenheit")
elif value=='f' or 'F':
    celsius_value=5/9*(temperature-32)
    print(value,"Fahrenheit is", celsius_value,"Celsius.")
else:
    print("Invalid")
