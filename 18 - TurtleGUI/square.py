from turtle import Turtle, Screen

michelangelo = Turtle()

for i in range(4):
    michelangelo.forward(100)
    michelangelo.right(90)


screen = Screen()
screen.exitonclick()
