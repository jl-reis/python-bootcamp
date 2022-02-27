from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.record = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} | Record: {self.record}", False, align="center", font=("Arial", 15, "normal"))

    def add_score(self):
        """Add score point to the Scoreboard"""
        self.score += 1
        self.update()

    def save_record_to_file(self):
        """Saves the record to file"""
        if self.score > self.record:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.record = self.score
        self.score = 0
        self.update()
