import turtle

import colorgram

# colors = colorgram.extract('imagee.jpg', 20)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_list.append((r, g, b))
#
# print(rgb_list)

from turtle import Turtle, Screen
import random

turtle.colormode(255)
rgb_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
            (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
            (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165),
            (215, 56, 27)]

tim = Turtle()
tim.speed("fastest")
tim.penup()

# to start at bottom of screen
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100
for dots in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(rgb_list))
    tim.forward(40)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)

tim.hideturtle()
screen = Screen()
screen.exitonclick()
