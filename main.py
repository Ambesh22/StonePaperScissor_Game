'''
1: Stone
-1: Paper
0: Scissor
'''
import random
computer = random.choice([1,-1,0])

print("Let's Play Stone_Paper_Scissor Game!")
youstr = input("Enter your choice for Stone(s),Paper(p) and Scissor(sc):")
yourDict = {"s":1, "p":-1, "sc":0}
you = yourDict[youstr]
reverseDict = {1:"Stone",-1:"Paper",0:"Scissor"}

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a Draw")
else:
    if (computer == 1 and you == -1): #Analysis to find pattern: Positive 0(sum 1 + -1)   Negative 2(1 - -1)
        print("You win!")
    elif (computer == 1 and you == 0): #1   1
        print("Computer win")
    elif (computer == -1 and you == 0): #-1  -1
        print("Computer win")
    elif (computer == -1 and you == 0): #-1   -1
        print("Computer win")
    elif (computer == 0 and you == 1): #1  -1
        print("You win!")
    elif (computer == 0 and you == -1): #-1  1
        print("computer win")
    else:
        print("Something went wrong..")

# if(computer - you)== 1 or (computer - you)== -1: # Good to replace above if-else ladder code using analysis but not readable.
#     print("Computer wins")
# elif (computer - you)==0:
#     print("Draw")
# else:
#     print("you win")
