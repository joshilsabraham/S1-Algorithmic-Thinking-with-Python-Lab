'''
Author - Joshil S Abraham
Date = 22/11/2024
Description: Program demonstrates merging two lists of integers, segregating the combined list into even and odd numbers, and then 
             sorting them separately. Finally, it displays the even and odd numbers in sorted order and prints a new merged list with 
             even numbers followed by odd numbers. This program uses loops and conditional statements for list manipulation.
'''
list_1 = [3,1,7,5,8]
list_2 = [10,6,9,4,2]
print('List-1 is',list_1)
print('List-2 is',list_2)
combined_list = list_1 + list_2        # Merging the list
print('The combined list is',combined_list)
even_numbers = []
odd_numbers = []
for i in combined_list:
    if i % 2 == 0:
        even_numbers.append(i)
        even_numbers.sort()
    else:
        odd_numbers.append(i)
        odd_numbers.sort()
print("Even numbers are",even_numbers)
print("Odd numbers are", odd_numbers)
print("The Merged List is",even_numbers+odd_numbers)
