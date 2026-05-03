import random
import numpy as np
import matplotlib.pyplot as plt

#this is a guess game
# There is competition and the one with the fewest guesses wins

x=random.randrange(1,100)
#x is a random integer between 1 and 100

for i in range(20):
    y=int(input("Enter your Lucky number   "))

    if x==y:
        print(f"You got it in {i+1} attempts ")
        break
    
    elif x>y:
        print("Too low")
    else:
        print("Too high")