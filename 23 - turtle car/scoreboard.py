from turtle import Turtle

FONT = ("Courier", 15, "normal")
POSITION = (-240, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        """Updates the scoreboard"""
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {self.level}", move=True, align="center", font=FONT)

    def up(self):
        """Increases the level"""
        self.level += 1
        self.update()

    def game_over(self):
        """Finishes the game"""
        self.goto((0, 0))
        self.write("GAME OVER", move=False, align="center", font=FONT)
