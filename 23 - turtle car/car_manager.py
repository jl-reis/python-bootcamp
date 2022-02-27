from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.velocity = 0

    def new_car(self):
        """Generates a new car"""
        new_car = Turtle()
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.hideturtle()
        new_car.goto((300, randint(-200, 230)))
        new_car.showturtle()
        self.cars.append(new_car)

    def move(self):
        """Moves all the cars"""
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + self.velocity)

    def level_pass(self):
        """Increases the cars velocity"""
        self.velocity += MOVE_INCREMENT

    def hits_turtle(self, turtle):
        """Checks if a car hit the turtle"""
        for car in self.cars:
            if car.distance(turtle) < 100:
                return True
            else:
                return False
