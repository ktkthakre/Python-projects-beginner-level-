"""
Make a rock-paper-scissors game where it is the player vs the computer.
The computer’s answer will be randomly generated, while the program will ask
the user for their input.
Rules:
    rock crushes scissors
    paper covers rock
    scissors cuts paper
"""

import random
rps = ['rock','paper','scissor']

print("------Welcome to the game of Rock-Paper-Scissors!!------")
while True:
    print("\nType you choice in front of shoot! Type 'q' to quit the game...")
    computer_choice = random.choice(rps)
    user_choice = input("\nRock-Paper-Scissor say shoot: ").lower()
    if user_choice == 'q':
        print("\nSorry to see you go! Have a nice day!")
        break
    else:
        print("\nComputer's choice: " + computer_choice)
        print("Your choice: " + user_choice)
        if computer_choice == user_choice:
            print("\n\tDraw!")
        else:
            if computer_choice == 'rock':
                if user_choice == 'paper':
                    print("\n\tPaper covers Rock: User wins!")
                elif user_choice == 'scissor':
                    print("\n\tRock crushes Scissors: Computer wins!")
            elif computer_choice == 'scissor':
                if user_choice == 'rock':
                    print("\n\tRock crushes Scissors: User wins!")
                elif user_choice == 'paper':
                    print("\n\tScissors cut Paper: Computer wins!")
            elif computer_choice == 'paper':
                if user_choice == 'scissor':
                    print("\n\tScissors cut Paper: User wins!")
                elif user_choice == 'rock':
                    print("\n\tPaper covers Rock: Computer wins!")
            else:
                print("\n\tInvalid input!")