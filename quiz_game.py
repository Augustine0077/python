# questions = (
#     "What is the capital of France?",
#     "Which planet is known as the Red Planet?",
#     "Who wrote 'Romeo and Juliet'?",
#     "What is the largest ocean on Earth?",
#     "What is the chemical symbol for water?",
#     "Which country is famous for the pyramids?"
# )

# options = (
#     ("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"),
#     ("A) Earth", "B) Mars", "C) Jupiter", "D) Venus"),
#     ("A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"),
#     ("A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"),
#     ("A) CO2", "B) H2O", "C) O2", "D) NaCl"),
#     ("A) India", "B) Mexico", "C) Egypt", "D) China")
# )

# answers = ("C", "B", "B", "D", "B", "C")
# guesses = []
# score = 0

# for question_num in range(len(questions)):
#     print("-------------------------")
#     print(questions[question_num])
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter (A, B, C, or D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("WRONG!")
#         print(f"{answers[question_num]} is the correct answer.")

# print("\nThe result is ---- >")
# print("answers:", end=" ")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses:", end=" ")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score_percent = int(score / len(questions) * 100)
# print(f"Your score is {score_percent}%")








questions=("What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest ocean on Earth?",
   "What is the chemical symbol for water?",
     "Which country is famous for the pyramids?")

options=(
    ("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"),
    ("A) Earth", "B) Mars", "C) Jupiter", "D) Venus"),
    ("A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"),
    ("A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"),
    ("A) CO2", "B) H2O", "C) O2", "D) NaCl"),
    ("A) India", "B) Mexico", "C) Egypt", "D) China")
)
answers = ("C", "B", "B", "D", "B", "C")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_number]} is the correct answer.")
    question_number += 1


print("---------------")
print("Results")
print("---------------")
print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percent = int(score / len(questions) * 100)
print(f"Your score is {score_percent}%")
score = score /len(questions) * 100

print(f"Your score is {score}%")