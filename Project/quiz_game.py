#quiz game
questions = ("What is the integration of sin(x)",
            "What is biggest country in the world",
            "What is the anime that have the main character Erin Yeager ",
            "Who is the mother of programming langues",
            "Where is the food pasta invented")

options = (("A.-sin(x) ","B.-cos(x) ","C.cos(x) ","D.tan(x)"),
          ("A.Russia","B.China","C.Usa","D.England"),
          ("A.One Punch man","B.Aot","C.Re.Zero","D.Akamiga kill"),
          ("A.Python","B.Ruby","C.R","D.C"),
          ("A.Italy","B.Spain","C.Egypt","D.Sudan"))

answers =("C","A","B","D","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct")

    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------")
print("      Results       ")
print("--------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is: {score}%")
