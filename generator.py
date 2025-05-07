import random
number=random.randint(1,6)
print(number)
options = ("rock","papaer","scissors")
print(random.choice(options))
#creating a number guessing game
lowest =1
highest =100
running = True
guesses =0
answer = random.randint(lowest,highest)
while running:
    guess = input(f"Guess a number from {lowest} and {highest}:")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < lowest or guess> highest:
            print("Guess is out of range")
            print(f"Plese Enter a number form {lowest} and {highest}")
        elif guess < answer:
            print("Too Low,Try again")
        elif guess > answer:
            print("Too high,Try again")
        else:
            print("Correct!!")
            print(f"It took your {guesses} guesses")
            running = False

    else:
        print("Invald guess!!!")
        print(f"Plese Enter a number form {lowest} and {highest}")