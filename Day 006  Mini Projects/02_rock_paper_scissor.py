'''
WORKFLOW OF PROJECT
1. Input from user(Rock, Paper, Scissor)
2. Computer Choice (Computer will choose randomly & not conditionally)
3. Print Result
The Python random module is used to generate pseudo-random numbers, which can be used to choose random options.

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = lose
Rock - Scissor = win

B- Paper
Paper - Paper = tie
Paper - Scissor = lose
Paper - Rock = win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = lose
Scissor - Paper = win

'''

import random

option_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter Your Move: ")
comp_choice = random.choice(option_list)

if (user_choice == comp_choice):
          print("Match Tie")
elif(user_choice == "Rock"):
        if(comp_choice == "Paper"):
                print("You Lose")
        else:
                print("You Win")
elif(user_choice == "Paper"):
        if(comp_choice == "Rock"):
                print("You Win")
        else:
                print("You Lose")
elif(user_choice == "Scissor"):
        if(comp_choice == "Rock"):
                print("You Lose")
        else:
                print("You win")
else:
        print("Invalid Input")

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")
print("Thankyou for playing.")