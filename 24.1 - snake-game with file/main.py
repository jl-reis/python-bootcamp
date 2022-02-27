from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

snake_alive = True

while snake_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Checks if the head eats the food
    if snake.head.distance(food) < 15:
        food.new_food()
        score.add_score()
        snake.grow()
        print(score.record)

    # Checks if the snake collide with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < - 300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.save_record_to_file()
        snake.reset()

    # Checks if the head collide with the body
    for snake_block in snake.snake_body[1:]:
        if snake.head.distance(snake_block) < 10:
            score.save_record_to_file()
            snake.reset()

screen.exitonclick()
