from quiz_data import questions, options, answers

score = 0  # to count correct answers

print("  Welcome to the Quiz Game  \n")

for i in range(len(questions)):
    print(questions[i])
    for opt in options[i]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is:", answers[i], "\n")

print(" Quiz Completed ")
print("Your final score is:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! You got all correct!")
elif score >= 3:
    print("Good job! Keep practicing!")
else:
    print("Study more and try again!")
