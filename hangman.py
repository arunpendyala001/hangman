import random

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

	while chance>0:
		print(chance,"lives left")
		cha = input("Enter your choice: ")
		print(cha.capitalize())
		idx = 0
		for idx,val in b:
			if cha.capitalize() == val:
				guess[idx]=cha

			# else:
			# 	chance=chance-1

		print(*guess)






elif a == 2:
	c = Cars[random.randint(0,(len(Cars)-1))]
	print(c)
