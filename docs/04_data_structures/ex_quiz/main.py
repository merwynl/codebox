
# Quiz game

questions = ("What is the capital of Japan?: ",
             "How many prefectures are there in Japan?: ",
             "What is the name of the current era in the year 2025?: ",
             "How many regions are there in Japan?: ",
             "What is the name of the southernmost region that is not Okinawa?: ",)

options = ( ("A. Kyoto","B. Osaka","C. Tokyo","D. Nara" ),
            ("A. 8", "B. 43", "C. 54", "D. 47"),
            ("A. Reiwa", "B. Kamakura", "C. Heisei", "D. Showa"),
            ("A. 47", "B. 8", "C. 43","D. 9"),
            ("A. Honshu", "B. Kanto", "C. Shikoku", "D. Kyushu"))

answers = ("C", "D", "A", "B", "D")
guesses = []
score = 0
question_num = 0


for question in questions:
    print ("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    print()
    guess = input("What's the answer? (enter A,B,C or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("INCORRRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

    print("-----------------------------")
    print("           RESULTS           ")
    print("-----------------------------")

print ("Answers: ", end = "")
for answer in answers:
    print(answer, end=" ")
print()

print ("Your guess: ", end = "")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

if score == 100:
    print(f"You scored a perfect mark of {score}%!")
else:
    print(f"Your total score is {score}!")