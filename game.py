import random

#this is a guess game
# There is competition and the one with the fewest guesses wins

x=random.randint(1,100)
#x is a random integer between 1 and 100

y=int(input("Enter your Lucky number   "))
#The user enters their lucky number

#The conditional statement

if x==y:
    print("You got it")
else:
    print("Try again")