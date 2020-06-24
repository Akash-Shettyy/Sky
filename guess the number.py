import random
number = random.randrange(1,50)
number_of_guess=1
print("you got 5 chance to guess the number")
guess= int(input("guess the number:",))
while number_of_guess < 5 :
	                    
	if guess < number :
		print(" you need to guess higher number")
		print("you got " + str(5-number_of_guess)+"  guess left")  
		guess= int(input("guess the number,again:",))
		number_of_guess=number_of_guess + 1
		
	elif guess > number :# change made
		print("you need to guess lower number")
		print("you got " + str(5-number_of_guess)+"  guess left")  
		guess =int(input("guess the number:",))
	
		number_of_guess= number_of_guess + 1
		
	elif guess==number :
			print ("you got the correct number")      
			break
	
	
if number_of_guess == 5:
	print("sorry you are out of chance ")

	
