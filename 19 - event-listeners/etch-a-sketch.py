from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def rotate_right():
    turtle.right(15)


def rotate_left():
    turtle.left(15)


def reset_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()
