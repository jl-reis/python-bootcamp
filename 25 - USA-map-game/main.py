import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("USA map game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()

states_df = pd.read_csv("50_states.csv")
states_list = states_df.state.to_list()

right_guesses = []
while len(right_guesses) < 50:
    player_guest = screen.textinput(title=f"{len(right_guesses)}/50 - Guess a state name",
                                    prompt="Type a State").title()

    # Checks if the player guest is right and put it on the map
    if player_guest in states_list:
        x = int(states_df.x[states_df.state == player_guest])
        y = int(states_df.y[states_df.state == player_guest])
        state_turtle.goto(x=x, y=y)
        state_turtle.write(player_guest, move=True, align="center", font=("Arial", 10, "normal"))
        right_guesses.append(player_guest)

    if player_guest == "End":
        break

# Saves all the states the player didn't guessed
states_not_guessed = [state for state in states_list if (state not in right_guesses)]

# Congratulate player if he remembered all states
if len(states_not_guessed) == 0:
    state_turtle.clear()
    state_turtle.goto(x=-15, y=5)
    state_turtle.write("What a true patriot!\nYou guesses them all!",  align="center", font=("Arial", 30, "normal"))
    screen.exitonclick()

# Print states not guessed
not_guessed_df = pd.DataFrame(states_not_guessed, columns=["state"])
print(not_guessed_df)
not_guessed_df.to_csv("states_not_guessed.csv")
