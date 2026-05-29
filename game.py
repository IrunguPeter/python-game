import random
import array as arr
import matplotlib.pyplot as plt

#this is a guess game
# There is competition and the one with the fewest guesses wins

d=int(input("Enter the number of players  "))
Scores=[]
Names=[]

for x in range(d):
    N=input("Enter your name   ")
    Names.append(N)


    x=random.randrange(1,100)
    #x is a random integer between 1 and 100

    for i in range(20):
        y=int(input("Select your lucky number between 1 and 100   "))

        if x==y:
            print(f"You got it in {i+1} attempts ")
            e=(1+1)
            Scores.append(e)
                  
            break

        elif x>y:
            print("Too low")
        else:
            print("Too high")

plt.bar(Names, Scores)
plt.show()