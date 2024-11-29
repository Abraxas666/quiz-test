print("Quiz informatica")
import random 
questions = (
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the color of the sky?"
)

answers = [
    "Paris",
    "4",
    "Blue"
]

print(random.choice(questions))
       

def run_quiz(questions, answers):
    score = 0
    for i in range(questions):
        print(random.choice(questions))
       
        user_answer = input(questions[i] + " ")
        if user_answer.lower() == answers[i].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect. The correct answer is " + answers[i])
    print(f"Your final score is {score}/{len(questions)}")


# menu_string = """
#    1: Question
#     1. option
#     2. option
#     3. option\n"""

# selection = int(input(menu_string))


# if selection == 1:
#     print("Wrong answer")

# elif selection == 2:
#     print("Wrong answer")
    
# elif selection == 3:
#     print("Right answer")

# else:
#     print("invalid input")


# Q1 = "xxxxxx"
# Q2 = "xxxxxx"
# Q3 = "xxxxxx"
# Q4 = "xxxxxx"
# Q5 = "xxxxxx"
# lista_domande = [Q1, Q2, Q3, Q4, Q5]
# lista_risposte_giuste = []

# from random import randint
# print(lista_domande.randint)


