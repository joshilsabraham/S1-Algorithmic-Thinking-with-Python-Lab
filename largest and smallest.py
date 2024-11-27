# To find the largest and smallest numbers from a given list of numbers
total=int(input("Total number of numbers="))
n=0
small=1
large=1
while n<total:
    n=n+1
    number=int(input("Enter number:"))
    if number<small:
        small=number
    if number>large:
        large=number
print("Largest Number:",large)
print("Smallest Number:",small)
