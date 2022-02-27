from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        """Update the scoreboard"""
        self.clear()
        self.goto(-100, 230)
        self.write(self.p1_score, True, "center", ('Courier', 20, "normal"))
        self.goto(100, 230)
        self.write(self.p2_score, True, "center", ('Courier', 20, "normal"))

    def p1_point(self):
        """Add point to player 1"""
        self.p1_score += 1
        self.update()

    def p2_point(self):
        """Add point to player 2"""
        self.p2_score += 1
        self.update()
