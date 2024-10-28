# Program to convert temperatures between Celsius and Fahrenheit.
while True:
    print("1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    option=int(input("Choose an Option:"))
    if option==1:
        temperature=float(input('Enter Temperature in Celsius:'))
        fahrenheit_value=(temperature*9/5)+32
        print(f"{temperature}Celsius is{fahrenheit_value}Fahrenheit")
    elif option==2:
        temperature=float(input('Enter Temperature in Fahrenheit:'))
        celsius_value=(temperature-32)*5/9
        print(f"{temperature}Fahrenheit is{celsius_value}Celsius")
    elif option==3:
        exit()
    else:
        print("Invalid Option")