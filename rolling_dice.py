# rolling_dice.py

import random

def roll_dice():
    # Generate a random number between 1 and 6
    result = random.randint(1, 6)
    return result

def main():
    # Roll the dice
    rolled_value = roll_dice()
    # Display the result
    print(f"You rolled a {rolled_value}!")

if __name__ == "__main__":
    main()
