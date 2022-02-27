from turtle import Turtle, Screen
from random import randint, choice
from Spirograph import random_pencolor

don = Turtle()
screen = Screen()
screen.colormode(255)


headings = [0, 90, 180, 270]


for steps in range(100):
    don.pencolor(random_pencolor())
    don.setheading(choice(headings))
    don.forward(30)
    # makes the width of the pen thicker each step
    pensize = don.pensize()
    pensize += 0.05
    don.pensize(pensize)
    random_pencolor()


screen.exitonclick()
