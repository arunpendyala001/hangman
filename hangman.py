import random
import string

a = int(input("Select a category\n1 Movies\n2 Cars \n"))
Movies = ["DARLING", "AVENGERS"]
Cars = ["FORD", "BENTLEY", "AUDI"]
if a == 1:
	b = Movies[random.randint(0,(len(Movies)-1))]
	chance = 7
	guess = [ ]
	for i in range (len(b)):
		guess.append("_")
	print(*guess)
	print("Start guessing")
	print(b)


	while chance>0:
		c = 1
		print(chance,"lives left")
		cha = input("Enter your choice: ")
		c = c + 1
		print(cha.capitalize())
		list(b)
		for idx,val in enumerate(b):
			print(val)
			if cha.capitalize() == val:
				guess[idx]=cha.capitalize()
				break
			# elif cha.capitalize() != val:
			# 	chance=chance-1
			else:
				chance = chance - 1
				continue

		print(*guess)






elif a == 2:
	c = Cars[random.randint(0,(len(Cars)-1))]
	print(c)
