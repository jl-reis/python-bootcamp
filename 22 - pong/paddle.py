from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.color("white")
        self.penup()
        self.speed("fast")
        self.setheading(90)
        self.setposition(x_cord, y_cord)

    def move_up(self):
        """Move the paddle up"""
        if self.ycor() < 250:
            self.forward(10)

    def move_down(self):
        """Move the paddle down"""
        if self.ycor() > -250:
            self.backward(10)
