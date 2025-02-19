# List of game functions or mini-games


import os
# import ffxiv_crafting_aide


# Guessing game from Programming with Mosh (YouTube vid)

def guessing_game():
	import random
	secret_number = random.randint(0, 10)
	guess_count = 0
	guess_limit = 3
	while guess_count < guess_limit:
		guess = int(input("What's your guess? "))
		if guess != secret_number:
			print("Try again.")
			guess_count += 1
		else:
			print("You've won!")
			break
	else:
		print(f"You've lost. Better luck next time!\nThe number was {secret_number!r}")


# car game from Programming with Mosh (YouTube vid)


def car_game():
	started = False
	while True:
		command = input("> ").lower()
		if command == "start":
			if started:
				print("Car is already running!")
			else:
				started = True
				print("Car started... ")
		elif command == "stop":
			if not started:
				print("Car is already stopped!")
			else:
				started = False
				print("Car stopped.")
		elif command == "help":
			print("""
start - to start the car
stop - to stop the car
quit - to exit
			""")
		elif command == "quit":
			break
		else:
			print("Sorry, I don't understand.")


# defining my own functions


def ffxiv():
	print("Sure thing!")
	os.startfile('C\\Users\\fetidapple\\Desktop\\FINAL FANTASY XIV ONLINE.lnk')
	crafting_aide = input("""Hey, since you've booted up FFXIV would you like to run the crafting aide? """).lower()
	if crafting_aide == "yes":
		from ffxiv_crafting_aide import ffxivcraftingaide
		ffxivcraftingaide(input("What you wanna craft? ").lower())
	else:
		print("Very well.")
