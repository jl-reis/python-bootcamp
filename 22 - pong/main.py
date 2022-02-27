from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle(-350, 0)
player_2 = Paddle(350, 0)

screen.onkey(fun=player_1.move_up, key="w")
screen.onkey(fun=player_1.move_down, key="s")
screen.onkey(fun=player_2.move_up, key="Up")
screen.onkey(fun=player_2.move_down, key="Down")

score = Score()

direction = 45
ball = Ball(direction)

game_is_on = True
while game_is_on:
    score_point = False

    while not score_point:
        screen.update()
        ball.move()
        time.sleep(0.01)
        # Bounce the ball if it hits the wall
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.wall_bounce()
            print(ball.heading())

        # Checks if the ball hit the paddle and bounce it back
        if (ball.distance(player_1) < 60) and (-340 < ball.xcor() < -330):
            ball.paddle_bounce()
            print(ball.heading())
        elif (ball.distance(player_2) < 60) and (330 < ball.xcor() < 340):
            ball.paddle_bounce()
            print(ball.heading())

        # Checks if the player misses the ball
        if ball.xcor() > 400:
            score_point = True
            ball.reset_location()
            score.p1_point()
        elif ball.xcor() < -400:
            score_point = True
            ball.reset_location()
            score.p2_point()


screen.exitonclick()
