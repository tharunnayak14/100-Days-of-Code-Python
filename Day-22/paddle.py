from turtle import Turtle

DISTANCE = 50


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.goto(position[0], position[1])

    def go_up(self):
        new_y_cor = self.paddle.ycor() + DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y_cor)

    def go_down(self):
        new_y_cor = self.paddle.ycor() - DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y_cor)
