import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.move_up, key="Up")

level = Scoreboard()

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly adds a car
    if randint(0, 11) > 8:
        car_manager.new_car()

    car_manager.move()

    if player.level_pass():
        level.up()
        car_manager.level_pass()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()
