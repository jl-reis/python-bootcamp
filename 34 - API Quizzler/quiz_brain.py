class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if there are questions left in the question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Asks next question"""

        self.current_question = self.question_list[self.question_number]
        print(self.current_question.text)
        print(self.current_question.answer)
        self.question_number += 1
        print(self.question_number)
        print(len(self.question_list))
        next_question_text = f"Q.{self.question_number}: {self.current_question.text}"
        return next_question_text

    def check_answer(self, user_answer):
        """Checks if the user answer is correct"""

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
