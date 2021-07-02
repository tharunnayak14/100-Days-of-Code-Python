from turtle import Screen, Turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for i in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)


for j in range(3, 20):
    tim.color(random.choice(colours))
    draw_shape(j)

screen = Screen()
screen.exitonclick()
