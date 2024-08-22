#RockPaperScissors
import random

# ASCII Shortcuts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Greeting
print("Welcome to this modest Rock Paper Scissors game")

# User and Comp choice 
userChoice = userChoice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))
while userChoice > 2 or str(userChoice).isdigit() == False:
    userChoice = int(input("All you had to do is type 0, 1, 2. Try Again Dummy: "))
compChoice = random.randint(0,2)

print("You Chose: ")
if userChoice == 0:
    print(rock)
elif userChoice == 1:
    print(paper)
elif userChoice == 2:
    print(scissors)

print("Computer chose: ")

if compChoice == 0:
    print(rock)
elif compChoice == 1:
    print(paper)
elif compChoice == 2:
    print(scissors)

if userChoice == 0:
    if compChoice == 1:
        print("YOU LOST!!!")
    elif compChoice == 2:
        print("I guess you won")
    else:
        print("You drew to a computer. I'd say that's a loss")
elif userChoice == 1:
    if compChoice == 2:
        print("YOU LOST!!!")
    elif compChoice == 0:
        print("I guess you won")
    else:
        print("You drew to a computer. I'd say that's a loss")
elif userChoice == 2:
    if compChoice == 0:
        print("YOU LOST!!!")
    elif compChoice ==1:
        print("I guess you won")
    else:
        print("You drew to a computer. I'd say that's a loss")





