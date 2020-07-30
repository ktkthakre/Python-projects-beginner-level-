"""
The Goal: Like the title suggests, this project involves writing a program that 
simulates rolling dice. When the program runs, it will randomly choose a number 
between 1 and 6. (Or whatever other integer you prefer — the number of sides on 
the die is up to you.) The program will print what that number is. It should 
then ask you if you’d like to roll again. For this project, you’ll need to set
 the min and max number that your dice can produce. For the average die, that
  means a minimum of 1 and a maximum of 6. You’ll also want a function that
   randomly grabs a number within that range and prints it.
"""
import random

def dice_roll():
    roll = random.randint(1,6)
    return roll

def player_game():
    print("Welcome, choose from below options:\n1.Roll the Dice\n2.Exit")
    choice = int(input("==>"))
    if choice == 1:
        print("Here's your roll: " + str(dice_roll()))
    while True:
        prompt = input("Would you like to roll again? (y/n) :")
        if prompt == 'Y' or prompt == 'y':
            print("Here's your roll: " + str(dice_roll()))
        else:
            print("Thank you for playing!!")
            break
player_game()