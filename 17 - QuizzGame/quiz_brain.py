class QuizBrain:
    def __init__(self, qb_question_list):
        self.question_number = 0
        self.question_list = qb_question_list
        self.score = 0

    def still_has_questions(self):
        """Checks if there are question in the question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Asks next question"""
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/"
                            f"False): ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        """Checks if the user answer is correct"""
        if user_answer == correct_answer:
            print("That's right!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")
