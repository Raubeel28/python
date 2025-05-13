import random

options=("rock","paper","scissors")

running=True
while running:
    computer = random.choice(options)
    player =None
    while player not in options:
        player=input("Pls enter a choice(rock,paper,scissors)")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player== computer:
        print("It is a tie")
    elif player =="rock" and computer == "scissors":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    elif player== "paper" and computer == "rock":
        print("You win")
    else:
        print("You loose")
    if not input("play again (yes or no)").lower() =="yes":
     running = False
print("Thanks for playing")