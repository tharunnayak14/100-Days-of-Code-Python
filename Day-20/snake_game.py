from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# turn off tracer
screen.tracer(0)

# create a snake object
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

# to automatically move the snake
while game_is_on:
    # if we update screen here, the screen updates after all the segments move
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
