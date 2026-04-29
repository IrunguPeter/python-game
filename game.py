import random

#this is a guess game
# There is competition and the one with the fewest guesses wins

x=random.randrange(1,100)
#x is a random integer between 1 and 100

def game():
    y=int(input("Input your LUcky number  "))

    print(x)

    if y==x:
        print("You got it")
        
    elif y>x:
        print("Too high")
    else:
        print("Too low")

for i in range (7):
    game()