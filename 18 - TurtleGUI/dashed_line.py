from turtle import Turtle, Screen

leo = Turtle()

for writing in range(20):
    leo.forward(10)
    if writing % 2 == 0:
        leo.penup()
    else:
        leo.pendown()

screen = Screen()
screen.exitonclick()