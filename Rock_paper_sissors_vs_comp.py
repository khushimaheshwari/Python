import random
#TO USE RANDOM

print("...rock...\n")
print("...paper...\n")
print("...sissors...\n")

#ENTER CHOICES
player = input("Enter player 1's choice: ")

num = random.randint(0,2)

if num == 0:
	computer = "rock"
elif num == 1:
	computer = "paper"
else:
	computer = "sissors"
print("computer chooses: " + computer)

#DECLRARING WINNER

if player == computer:
		print("TRY AGAIN, ITS A TIE!")

elif player == "rock":
	if computer == 'paper':
		print("computer wins!")
	elif computer == 'sissors':
		print("player wins!")

elif player == "paper":
	if computer == 'rock':
		print("player wins!")
	elif computer == 'sissors':
		print("computer wins!")	
elif player == 'sissors':
	if computer == 'sissors':
		print("TRY AGAIN!")
	elif computer == 'rock':
		print("computer wins!")
	elif computer == 'paper':
		print("player wins!")	
else:
	print("enter choice again!")		