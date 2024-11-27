'''
Author: Joshil S Abraham
Date: 28/10/2024
Description: Program to simulate a simple bank ATM system.
'''
balance_amount=1000
while True:
    print("1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        print(f"The Balance Amount is ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Amount to be Deposited:"))
        balance_amount=balance_amount+deposit_amount
        print("")
    elif choice==3:
        withdrawn_amount= float(input("Amount to be Withdrawn:"))
        if balance_amount<withdrawn_amount:
            print("Insufficient Balance")
        else:
            balance_amount=balance_amount-withdrawn_amount
            print("")
    elif choice==4:
        break
    else:print("Invalid Entry")
