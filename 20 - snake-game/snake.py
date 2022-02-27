from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x = 0
        y = 0
        for snake_block in range(0, 3):
            snake_block = Turtle(shape="square")
            snake_block.penup()
            snake_block.color("white")
            snake_block.setposition(x, y)
            self.snake_body.append(snake_block)
            x -= 20

    def move(self):
        """Moves the snake forward"""
        for _ in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[_].goto(self.snake_body[_ - 1].pos())
        self.head.forward(20)

    def turn_up(self):
        """Turn the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def turn_down(self):
        """Turn the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def turn_left(self):
        """Turn the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def turn_right(self):
        """Turn the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def grow(self):
        """Add another block to the tail of the snake"""
        snake_block = Turtle(shape="square")
        snake_block.penup()
        snake_block.color("white")
        snake_block.setposition(self.snake_body[-1].pos())
        self.snake_body.append(snake_block)
