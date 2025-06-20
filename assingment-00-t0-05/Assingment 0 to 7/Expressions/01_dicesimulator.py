"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6  

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)  
    total = die1 + die2  
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")

def main():
    die1 = 10  
    print(f"die1 in main() starts as: {die1}")

    for _ in range(3):
        roll_dice()

    print(f"die1 in main() is still: {die1}")  
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()