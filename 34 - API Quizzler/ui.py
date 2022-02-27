from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzlerUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.quiz = quiz_brain

        # Score label
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        # Question canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=285
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_button_img,
            highlightthickness=0,
            command=self.check_is_true)
        self.true_button.grid(column=1, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_button_img,
            highlightthickness=0,
            command=self.check_is_false)
        self.false_button.grid(column=0, row=2)

        self.ask_next_question()

        self.window.mainloop()

    def ask_next_question(self):
        self.canvas.itemconfig(self.question, text=self.quiz.next_question())

    def check_is_true(self):
        if self.quiz.check_answer("True"):
            self.add_score()
            self.background_feedback("green")
        else:
            self.background_feedback("red")
        self.window.after(1000, self.check_end_game)

    def check_is_false(self):
        if self.quiz.check_answer("False"):
            self.add_score()
            self.background_feedback("green")
        else:
            self.background_feedback("red")
        self.window.after(1000, self.check_end_game)

    def check_end_game(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.ask_next_question()
        else:
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
            self.canvas.itemconfig(
                self.question,
                text="You've completed the quiz!\n"
                     f"Your final score was: {self.score}/{self.quiz.question_number}"
            )
            self.window.after(2000, self.window.quit)

    def add_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def background_feedback(self, feedback_color):
        self.canvas.config(bg=feedback_color)
