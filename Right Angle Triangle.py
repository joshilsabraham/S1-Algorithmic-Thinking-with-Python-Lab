'''
Author: Joshil S Abraham
Date: 29/11/2024
Description: A program that accepts the lengths of three sides of a triangle as inputs and gives the 
             output whether or not the triangle is a right triangle.(Using Pythagorean Theorem)
'''
def check_right_angled():
    length_1 = int(input("Enter Length:" ))
    length_2 = int(input("Enter Length:" ))
    length_3 = int(input("Enter Length:" ))
    sides=[length_1, length_2, length_3]
    base= min(sides)
    hypotenuse= max(sides)
    sides.remove(base)
    sides.remove(hypotenuse)
    altitude= sides[0]
    if (base ** 2) + (altitude ** 2) == (hypotenuse **2):
        return True
if check_right_angled()== True:
    print("For the given lengths, the resulting triangle is a right angled triangle")
else:
    print(""For the given lengths, the resulting triangle is not a right angled triangle")
