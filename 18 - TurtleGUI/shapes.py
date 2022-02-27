from turtle import Turtle, Screen
from random import randint

rafa = Turtle()
screen = Screen()
screen.colormode(255)


def random_pencolor():
    """Generates a random pencolor"""
    color1 = randint(0, 256)
    color2 = randint(0, 256)
    color3 = randint(0, 256)
    rafa.pencolor(color1, color2, color3)


random_pencolor()
for sides in range(3, 11):
    for draw in range(sides):
        rafa.forward(75)
        rafa.right(360/sides)
    random_pencolor()


screen.exitonclick()
