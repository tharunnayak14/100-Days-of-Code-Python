from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race")

colours = ["red", "orange", "pink", "green", "blue", "purple"]
# turtle screen centre co-ordinate = (0, 0)

all_turtles = []
i = 0
for color in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 50 * i)
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        # use 230 instead of 250 as turtle itself has size 40 x 40
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won, {winning_color} turtle is the winner")
            else:
                print(f"You Lose, {winning_color} turtle is the winner")

        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()
