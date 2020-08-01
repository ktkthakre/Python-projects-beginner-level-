import random

random_number = random.randint(1,20)

user_guess = int(input("Try guessing any number between 1 to 20: "))
if user_guess == random_number:
    print("Correct!")
else:
    wrong_guess = int(input("Wrong! Guess again: "))
    while True:
        if wrong_guess < random_number:
            wrong_guess = int(input("Go a little higher: "))
            continue
        elif wrong_guess > random_number:
            wrong_guess = int(input("Go a little lower: "))
            continue
        elif wrong_guess == random_number:
            print("Correct!! The number was " + str(random_number))
            break