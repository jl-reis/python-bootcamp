from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(direction)

    def move(self):
        self.forward(1)

    def wall_bounce(self):
        """Checks where the ball is heading and bounce it"""
        if 90 <= self.heading() <= 270:
            if self.ycor() > 0:
                self.setheading(self.heading() + randint(80, 100))
            else:
                self.setheading(self.heading() - randint(80, 100))
        else:
            if self.ycor() > 0:
                self.setheading(self.heading() + randint(260, 280))
            else:
                self.setheading(self.heading() - randint(260, 280))

    def paddle_bounce(self):
        """Checks where the ball is heading and bounce it"""
        if self.xcor() < 0:
            if 90 < self.heading() <= 180:
                self.setheading(self.heading() - randint(80, 100))
            elif 180 < self.heading() <= 270:
                self.setheading(self.heading() + randint(80, 100))
        if self.xcor() > 0:
            if 0 <= self.heading() < 90:
                self.setheading(self.heading() + randint(80, 100))
            elif 270 <= self.heading() < 360:
                self.setheading(self.heading() - randint(80, 100))

    def reset_location(self):
        """Return the ball to the start location"""
        random_direction = randint(135, 225)
        if self.xcor() > 400:
            self.goto(0, 0)
            if random_direction > 180:
                self.setheading(180 - random_direction)
            else:
                self.setheading(180 + random_direction)
        elif self.xcor() < -400:
            self.goto(0, 0)
            self.setheading(random_direction)
