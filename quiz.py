questions = ("How many elements are the periodic table?:",
             "Which animal lays the largest eggs?",
             "Which gas is the most abundant in the Earth's atmosphere?",
             "How many bones are there in the human body",
             "Which planet is the hottest in the solar system")
options = (("A.446","B.476","C.487","D.487"),
           ("A.crocodile","B.whale","C.elephant","D.ostrich"),
           ("A.Nitrogen","B.Oxygen","C.Neon","D.Hydrogen"),
           ("A.206","B.207","C.205","D.209"),
           ("A.Mercury","B.Venus","C.Earth","D.Mars"))
answers=("B","D","D","B","A")
guesses = []
score = 0
question_no =0

for question in questions:
    print("---------")
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        print("CORRECT")
        score +=1
    else:
        print("INCORRECT")
        print(f"{answers[question_no]} is the correct answer")
        

    question_no +=1
print("guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()

print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your score is:{score}%")