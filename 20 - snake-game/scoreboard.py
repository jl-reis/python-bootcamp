from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def add_score(self):
        """Add score point to the Scoreboard"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        """Finish game"""
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 20, "normal"))
