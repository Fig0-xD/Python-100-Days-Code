class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def ask_question(self):
        user_answer = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].text}"
                            " (True/False)?: ").lower()

        self.check_answer(user_answer, self.question_list[self.question_number].answer)

        self.question_number += 1

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right! 👏")
            self.score += 1
        else:
            print("That's wrong ☹")

        print(f"The correct answer was: {answer}")
        print(f"Your current score: {self.score}/{self.question_number + 1}")
        print("\n")