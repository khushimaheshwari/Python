import random
#Guessing game
random_number = random.randint(1,10)
number = None
while number != random_number:		
	number = int(input("GUESS A NUMBER \n"))
	if number < random_number:
		print("Too Low,try Again")
	elif number > random_number:
		print("Too High,try Again")
	else:
		print(" CORRECT CHOICE.YOU WON!")
print(random_number)		
