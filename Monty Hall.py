'''
Author: Joshil S Abraham
Date: 06/12/2024
Description: Suppose you're on a game show, and you are given the choice of three doors: 
             Behind one door is a car; behind the others, goats. You pick a door, say No. 1,
             and the host, who knows what is behind the doors, opens another door, say No. 3, 
             which has a goat. He then asks, "Do you want to pick door No. 2?" 
             Is it to your advantage to switch your choice?
'''
import random
def monty_hall_game():
   # Randomly place the car behind one of the three doors
    doors = [0, 0, 0]  # 0 for goat, 1 for car
    car_position = random.randint(0, 2)
    doors[car_position] = 1
  
  # Display doors to the player
    print("Welcome to the Monty Hall Game Show!")
    print("There are three doors: Door 1, Door 2, and Door 3.")
    print("Behind one door is a car, and behind the other two are goats.")
   
  # Player makes an initial choice
    player_choice = -1
    while player_choice not in [1, 2, 3]:
        player_choice = input("Pick a door (1, 2, or 3): ")
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if player_choice not in [1, 2, 3]:
                print("Invalid input. Choose a number between 1 and 3.")
        else:
            print("Invalid input. Enter a valid number.")
            player_choice = -1
    player_choice -= 1  # Convert to 0-based index

  # Host reveals a door with a goat
    possible_doors_to_open = [i for i in range(3) if i != player_choice and doors[i] == 0]
    host_opens = random.choice(possible_doors_to_open)

    print(f"The host opens Door {host_opens + 1} and reveals a goat!")

    # Player decides whether to switch
    switch_choice = ""
    while switch_choice not in ["yes", "no"]:
        switch_choice = input("Do you want to switch to the other unopened door? (yes/no): ").strip().lower()
        if switch_choice not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Determine final choice
    if switch_choice == "yes":
        final_choice = [i for i in range(3) if i != player_choice and i != host_opens][0]
    else:
        final_choice = player_choice

    # Reveal the result
    if doors[final_choice] == 1:
        print(f"Congratulations! You won the car behind Door {final_choice + 1}!")
    else:
        print(f"Sorry, you got a goat behind Door {final_choice + 1}.")

# Start the game
monty_hall_game()
