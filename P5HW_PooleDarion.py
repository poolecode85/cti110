# Darion Poole
# 05/6/25
# P5HW
# Use of loops, functions and module import to create a home run derby game

import random

# Function to create a character
def create_character():
    print("Welcome to the Home Run Derby!")
    name = input("Enter your character's name: ")

    print("\nYou have 15 points to assign to Power, Accuracy, and Stamina.")

    power = int(input("Points to Power (1-10): "))
    accuracy = int(input("Points to Accuracy (1-10): "))
    stamina = int(input("Points to Stamina (1-10): "))

    total = power + accuracy + stamina

    if total > 15 or power < 1 or accuracy < 1 or stamina < 1:
        print("Invalid input! Please restart the game and follow the rules.")
        return None  # Stops the game if inputs are wrong

    return {
        "name": name,
        "power": power,
        "accuracy": accuracy,
        "stamina": stamina
    }

# Function to run the derby
def take_swings(player):
    swings = player["stamina"] * 2
    home_runs = 0
    print(f"\n{player['name']} gets {swings} swings!")

    for i in range(1, swings + 1):
        power_roll = random.randint(1, 10)
        accuracy_roll = random.randint(1, 10)

        player_average = (player["power"] + player["accuracy"]) / 2
        roll_average = (power_roll + accuracy_roll) / 2

        if roll_average >= player_average:
            home_runs += 1
            print(f"Swing {i}: HOME RUN!")
        else:
            print(f"Swing {i}: Missed.")

    print(f"\nTotal Home Runs: {home_runs}")

# Main function to play the game
def play_game():
    player = create_character()
    if player is not None:
        take_swings(player)

        print("\nDo you want to play again?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            play_game()  # Calls itself once if player wants to play again
        else:
            print("Thanks for playing!")


# Start the game
play_game()
