from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
for i in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()