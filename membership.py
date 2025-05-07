word = "APPLE"
letter = input("Guess a leltter in the secret word").upper()
if letter in word:
    print(f"Yes!!!,there was {letter} in the word")
else:
    print(f"The was no {letter} in the word")

students = {"Spongebob","patrick","Esi"}
student = input("Enter a name of a student")
if student in students:
    print(f"{student} is among the students")
else:
    print(f"{student} is not among the students")

grades = {
    "sonny": "A",
    "patrick":"B",
    "Henry":"C"
}
if student in grades:
    print(f"{student}'s grade is {grades[student]}")

email = "Bro@gmail.com"
if "@" in email and  ".com" in email:
    print("Valid email")
else:
    print("Invalid email")