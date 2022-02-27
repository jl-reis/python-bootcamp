import colorgram
from turtle import Turtle, Screen
from random import choice


def extract_color(number_of_colors):
    """Extract the n number of the more frequent colors"""

    extracted_colors = colorgram.extract('image.jpg', number_of_colors)
    colors = []
    for color in extracted_colors:
        color_extracted = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors.append(color_extracted)
    colors = colors[4:]
    return colors


def get_dots_coordinates(screen_height, screen_width):
    """Returns the dots coordinates based on the size of the screen"""
    dots_coordinates = []
    x = int(screen_width/11)
    y = int(screen_height/11)
    for _ in range(10):
        for _ in range(10):
            dots_coordinates.append((x, y))
            x += int(screen_width/11)
        y += int(screen_height/11)
        x = int(screen_width / 11)
    return dots_coordinates


turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
screen = Screen()
screen.colormode(255)
height = screen.window_height()
width = screen.window_width()
# print(height)
# print(width)
screen.setworldcoordinates(0, 0, width, height)

rgb_colors = extract_color(30)

# print(get_dots_coordinates(height, width))

for coordinates in get_dots_coordinates(height, width):
    turtle.penup()
    turtle.goto(coordinates)
    turtle.hideturtle()
    turtle.dot(20, choice(rgb_colors))


screen.exitonclick()
