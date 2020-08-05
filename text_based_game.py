"""
This is a text based game.
Please give answers exactly as the choices (in lower case)
"""
print("Welcome to this game!")
while True:
	answer = input("Would you like to play? (yes/no): ")
	if answer == "yes":
		print("You were unconcious and woke up at a strange place!")
		answer = input("There are two doors in front of you! Pick one (right/left): ")
		if answer == 'right':
			print("You open the door and a large boulder falls on you! Sorry, you are dead!")
			break
		elif answer == 'left':
			print("You win!")
			break
		else:
			print("Invalid input! Game over!")
			break
	else:
		answer = input("Really? (yes/no): ")
		if answer == 'yes':
			break
		else:
			continue