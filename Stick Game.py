'''
Author: Joshil S Abraham
Date: 06/12/2024
Description: Write a program to play a sticks game in which there are 16 sticks. 
             Two players take turns to play the game. 
             Each player picks one set of sticks (needn’t be adjacent) during his turn. 
             A set contains 1, 2, or 3 sticks. 
             The player who takes the last stick is the loser. 
             The number of sticks in the set is to be input.
'''
print("Welcome to Stick Game\n")
print("Rules:")
print("* Two players take turns to play the game")
print("* Each player picks one set of sticks")
print("* A set can contain 1, 2, or 3 sticks")
print("* The player who takes the last stick is the loser\n")

# Get player names
player1 = input("Enter name of Player-1: ")
player2 = input("Enter name of Player-2: ")

number_of_sticks = 16

while number_of_sticks > 0:
    print(f"\nSticks remaining: {number_of_sticks}")

    # Player 1's turn
    print(f"{player1}, choose your set of sticks (1, 2, or 3): ", end="")
    sticks_taken = int(input())
    if sticks_taken < 1 or sticks_taken > 3 or sticks_taken > number_of_sticks:
        print("Invalid choice. Please pick a valid number of sticks.")
        continue
    number_of_sticks -= sticks_taken

    if number_of_sticks == 0:
        print(f"\n{player1} lost. Better luck next time!")
        print(f"{player2}, You won!")
        break

    print(f"\nSticks remaining: {number_of_sticks}")

    # Player 2's turn
    print(f"{player2}, choose your set of sticks (1, 2, or 3): ", end="")
    sticks_taken = int(input())
    if sticks_taken < 1 or sticks_taken > 3 or sticks_taken > number_of_sticks:
        print("Invalid choice. Please pick a valid number of sticks.")
        continue
    number_of_sticks -= sticks_taken

    if number_of_sticks == 0:
        print(f"\n{player2} lost. Better luck next time!")
        print(f"{player1}, You won!")
        break
