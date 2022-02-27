from turtle import Turtle, Screen
from random import choice, randint

# Create turtle racers
don = Turtle()
leo = Turtle()
rafa = Turtle()
mike = Turtle()
jon = Turtle()
screen = Screen()
screen.setup(height=500, width=600)
screen.colormode(255)


def move_forwards(turtle):
    turtle.forward(10)


race_finish = False
players_bet = screen.textinput("Place your bet", "Who do you think will win?")
racers = [don, mike, rafa, leo, jon]
colors = ["orange", "red", "blue", "purple", "yellow"]
winner = None
y = -100

for racer in racers:

    # Set different color to each racer
    racer.color(colors[racers.index(racer)])
    racer.speed("slowest")
    racer.shape("turtle")
    racer.penup()

    # Send racer to start line
    racer.goto(-270, y)
    y += 50

while not race_finish:

    # Choose racer to move forward
    choice(racers).forward(randint(0, 10))
    for racer in racers:

        # Finish race if racers cross the finish line
        if racer.xcor() == 270:
            race_finish = True
            winner = racer

if players_bet == winner.color()[1]:
    print("You bet right! Congrats")
else:
    print(f"You bet wrong. The winner is {winner.color()[1]}")


screen.exitonclick()
