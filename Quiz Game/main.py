from random import choice
from data import q_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo


def quiz():

    question_bank = []
    question_data = choice(q_data)

    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))

    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.ask_question()

    print("\nYou have completed the quiz")
    print(f"Your final score is: {quiz_brain.score}/{len(question_bank)}")

if __name__ == "__main__":
    print(logo)
    quiz()