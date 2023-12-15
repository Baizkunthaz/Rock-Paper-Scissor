import random

options = ["Rock", "Paper", "Scissors"]

You = input("Choose Rock, Paper, or Scissors: ")
Comp = random.choice(options)

print("You chose: ", You)
print("Computer chose: ", Comp)

if You == Comp:
    print("It's a tie!")
elif You == "Rock" and Comp == "Scissors":
    print("You win!")
elif You == "Paper" and Comp == "Rock":
    print("You win!")
elif You == "Scissors" and Comp == "Paper":
    print("You win!")
else:
    print("Computer wins!")