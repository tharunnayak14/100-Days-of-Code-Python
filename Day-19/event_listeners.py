from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
# only moves when space key is pressed
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
