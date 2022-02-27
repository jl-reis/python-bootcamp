from turtle import Turtle, Screen
from random import randint

don = Turtle()
don.speed(0)
screen = Screen()
screen.colormode(255)


def random_pencolor():
    """Returns the tuple with the RGB of a random color"""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color


for angle in range(90):
    don.setheading(angle*4)
    don.pencolor(random_pencolor())
    don.circle(100)


screen.exitonclick()
