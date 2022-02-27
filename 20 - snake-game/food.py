from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def new_food(self):
        """Generate a new food in a random location"""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
