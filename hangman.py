import random

def chances(c):
	if c == 0:
		print("You've lost try again")
	else:
		print("You've won!")

def work(choice):
	b = choice[random.randint(0,(len(choice)-1))]
	chance = 7
	guess = [ ]
	for i in range (len(b)):
		guess.append("_")
	print(*guess)
	print("Start guessing")

	while chance>0 and "_" in guess:
		print(chance,"lives left")
		cha = input("Enter your choice: ")
		found = False
		for idx,val in enumerate(b):
			if cha.capitalize() == val:
				guess[idx]=cha.capitalize()
				found = True
		if found == False:
			chance = chance - 1

		print(*guess)

	chances(chance)




a = int(input("Select a category\n1 Movies\n2 Cars \n"))
Movies = ["DARLING", "AVENGERS"]
Cars = ["FORD", "BENTLEY", "AUDI"]

if a == 1:
	work(Movies)

elif a == 2:
	work(Cars)
