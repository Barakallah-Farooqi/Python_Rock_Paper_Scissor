# Rock Paper Scissor Shoot
# Rock    =  1
# Paper   = -1
# Scissor =  0

import random
computer = random.choice([1,-1,0])
you_rrr = input("Enter R for Rock P for Paper S for Scissor: ")
you_meow = {"R":1,"P":-1,"S":0}
you = you_meow[you_rrr]
reverse_meow = {1:"Rock",-1:"Paper",0:"Scissor"}
print(f"The value entered by you is {reverse_meow[you]}: \n The value entered by computer is {reverse_meow[computer]}")
if (computer == you):
    print("Draw match Try again:(( ")
else:
    if(computer == 1 and you == -1):
        print("You Win")
    elif(computer == 1 and you == 0):
        print("You Lose")
    elif(computer == -1 and you == 0):
        print("You Win")
    elif(computer == -1 and you == 1):
        print("You Lose")
    elif(computer == 0 and you == 1):
        print("You Win")
    elif(computer == 0 and you == -1):
        print("You Lose")
    
